import numpy as np
import time
import tracemalloc
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sieve import eratosthenes_sieve, initialize_prime_weights
from activations import fermat_activation_vec
from rsa_wrapper import generate_rsa_keys, encrypt_data_vec as encrypt_data

def compute_classification_metrics(y_true, y_pred):
    """
    Computes standard machine learning classification metrics.
    """
    y_true = np.array(y_true).flatten()
    y_pred = np.array(y_pred).flatten()
    
    accuracy = np.mean(y_true == y_pred)
    
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    
    return {
        "Accuracy": float(accuracy),
        "Precision": float(precision),
        "Recall": float(recall),
        "F1-Score": float(f1)
    }

class BaselineIntegerMLP:
    """
    A standard integer-weight baseline MLP for comparative performance benchmarking.
    """
    def __init__(self, input_dim, hidden_dim, output_dim, modulus=1009):
        self.modulus = modulus
        np.random.seed(42)
        self.W1 = np.random.randint(1, 50, size=(hidden_dim, input_dim))
        self.b1 = np.zeros(hidden_dim, dtype=int)
        self.W2 = np.random.randint(1, 50, size=(output_dim, hidden_dim))
        self.b2 = np.zeros(output_dim, dtype=int)
        
    def predict(self, X):
        preds = []
        for x in X:
            z1 = np.dot(self.W1, x) + self.b1
            a1 = np.maximum(0, z1) % self.modulus
            z2 = np.dot(self.W2, a1) + self.b2
            preds.append(1 if (z2[0] % 2 == 0) else 0)
        return np.array(preds)

def run_real_world_comparison():
    print("==================================================")
    print("   REAL IRIS COMPARATIVE BENCHMARK EVALUATION     ")
    print("==================================================\n")
    
    # 1. Load actual Iris dataset and scale floating-point features into safe integers
    iris = load_iris()
    X_raw_float = iris.data
    y_raw = iris.target
    
    # Convert multi-class labels into a binary classification task (0 vs 1,2)
    y_binary = np.array([0 if label == 0 else 1 for label in y_raw])
    
    # Scale features by 100 to map continuous measurements into clean integer inputs
    X_integers = np.round(X_raw_float * 100).astype(int)
    
    # Split into train/test sets to evaluate generalization on real data
    _, X_test, _, y_test = train_test_split(X_integers, y_binary, test_size=0.3, random_state=42)
    
    # 2. Benchmark Baseline Integer MLP
    print("Evaluating Baseline Integer MLP on Iris Test Split...")
    baseline = BaselineIntegerMLP(input_dim=4, hidden_dim=4, output_dim=1)
    
    tracemalloc.start()
    start_t = time.perf_counter()
    baseline_preds = baseline.predict(X_test)
    end_t = time.perf_counter()
    _, baseline_ram = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    baseline_latency = (end_t - start_t) / len(X_test) * 1000
    baseline_metrics = compute_classification_metrics(y_test, baseline_preds)
    
    # 3. Benchmark Number-Theoretic Neural Network using exact network.py forward architecture
    print("Evaluating Number-Theoretic Neural Network (Ours - network.py forward architecture)...")
    prime_pool = eratosthenes_sieve(2000)
    dim = 4
    p1, p2, p3 = 997, 1009, 1013
    
    W1 = initialize_prime_weights(dim, dim, prime_pool)
    W2 = initialize_prime_weights(dim, dim, prime_pool[10:])
    W3 = initialize_prime_weights(dim, dim, prime_pool[20:])
    
    b1 = np.array([0, 0, 0, 0])
    b2 = np.array([0, 0, 0, 0])
    b3 = np.array([0, 0, 0, 0])
    
    pub_key, _ = generate_rsa_keys(p=61, q=53)
    
    # Exact network.py forward pass mechanism
    def network_2_forward(w1, w2, w3, x_encrypted):
        z1 = (np.dot(w1, x_encrypted) + b1) % p1
        a1 = (fermat_activation_vec(z1, p1) + z1) % p1
        z2 = (np.dot(w2, a1) + b2) % p2
        a2 = (fermat_activation_vec(z2, p2) + z2) % p2
        z3 = (np.dot(w3, a2) + b3) % p3
        a3_balanced = z3 % 2
        return a3_balanced

    tracemalloc.start()
    start_t = time.perf_counter()
    ours_preds = []
    for row in X_test:
        x_enc = np.array(encrypt_data(row, pub_key))
        a3_balanced = network_2_forward(W1, W2, W3, x_enc)
        ours_preds.append(1 if np.mean(a3_balanced) > 0.5 else 0)
        
    end_t = time.perf_counter()
    _, ours_ram = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    ours_latency = (end_t - start_t) / len(X_test) * 1000
    ours_metrics = compute_classification_metrics(y_test, ours_preds)
    
    print("\n==================================================")
    print("         COMPARATIVE PERFORMANCE RESULTS          ")
    print("==================================================")
    print(f"{'Architecture':<26} | {'Accuracy':<8} | {'F1-Score':<8} | {'Latency':<10} | {'RAM':<8}")
    print("-" * 68)
    print(f"{'Baseline Integer MLP':<26} | {baseline_metrics['Accuracy']*100:.1f}%    | {baseline_metrics['F1-Score']:.4f}   | {baseline_latency:.4f}ms | {baseline_ram/1024:.2f}KB")
    print(f"{'Number-Theoretic (Ours)':<26} | {ours_metrics['Accuracy']*100:.1f}%    | {ours_metrics['F1-Score']:.4f}   | {ours_latency:.4f}ms | {ours_ram/1024:.2f}KB")
    print("==================================================")

if __name__ == "__main__":
    run_real_world_comparison()