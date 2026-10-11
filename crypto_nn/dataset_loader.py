import numpy as np
import math
from sieve import eratosthenes_sieve

def is_prime_check(n):
    """Simple quick scalar primality check for dataset labeling optimization."""
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def generate_prime_density_data(num_samples=20, feature_dim=4, value_range=(10, 200)):
    """
    Generates a structured, asymmetric dataset for testing the network's boundaries.
    
    Target Label Configuration:
    - 1 if the input row contains 2 or more prime numbers.
    - 0 if the input row is dominated by composite numbers.
    """
    np.random.seed(42)  # Lock randomness for consistent evaluation runs
    
    # Generate random integer values within a safe RSA-compatible boundary
    X_raw = np.random.randint(value_range[0], value_range[1], size=(num_samples, feature_dim))
    Y_targets = np.zeros((num_samples, feature_dim), dtype=int)
    
    for idx, row in enumerate(X_raw):
        # Calculate how many prime elements exist in this sample array
        prime_count = sum(1 for val in row if is_prime_check(val))
        
        # Labeling mapping step:
        # If prime density is high, map the balanced target objective pattern to [1, 0, 1, 0]
        # If composite density is high, map the target objective pattern to [0, 1, 0, 1]
        if prime_count >= 2:
            Y_targets[idx] = np.array([1, 0, 1, 0])
        else:
            Y_targets[idx] = np.array([0, 1, 0, 1])
            
    return X_raw.tolist(), Y_targets

if __name__ == "__main__":
    print("Testing Synthetic Dataset Production...")
    features, targets = generate_prime_density_data(num_samples=3)
    
    for i in range(len(features)):
        print(f"Sample #{i+1} | Raw Inputs: {features[i]} -> Configured Target Objective: {targets[i].tolist()}")
