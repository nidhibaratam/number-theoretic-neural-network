import numpy as np
from sieve import eratosthenes_sieve, initialize_prime_weights
from activations import fermat_activation_vec
from rsa_wrapper import generate_rsa_keys, encrypt_data_vec as encrypt_data
from optimization import compute_riemann_gradients_fast, move_prime_steps_fast
from dataset_loader import generate_prime_density_data

def print_weight_migration(W_old, W_new, layer_name):
    """Prints a beautiful visual map of weight parameter movements with directional arrows."""
    print(f"\n{layer_name} WEIGHT MIGRATION MAP:")
    print("-" * 60)
    for i in range(W_old.shape[0]):
        row_str = []
        for j in range(W_old.shape[1]):
            old_p = W_old[i, j]
            new_p = W_new[i, j]
            
            # Establish the visual arrow movement indicator
            if new_p > old_p:
                arrow = "▲" # Scaled up to a higher prime
            elif new_p < old_p:
                arrow = "▼" # Dropped down to a lower prime
            else:
                arrow = "•" # Held structural position
                
            row_str.append(f"[{old_p:3d} {arrow} {new_p:3d}]")
        print("   ".join(row_str))
    print("-" * 60)

def train_network_on_dataset():
    print("==================================================")
    print("   DEEP CRYPTO NN: VISUAL MIGRATION TRAINING LOOP")
    print("==================================================")
    
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
    raw_dataset, target_dataset = generate_prime_density_data(num_samples=10)
    print(f"Loaded {len(raw_dataset)} sample rows successfully.\n")
    
    def forward_pass(w1, w2, w3, x_encrypted):
        z1 = (np.dot(w1, x_encrypted) + b1) % p1
        a1 = (fermat_activation_vec(z1, p1) + z1) % p1
        z2 = (np.dot(w2, a1) + b2) % p2
        a2 = (fermat_activation_vec(z2, p2) + z2) % p2
        z3 = (np.dot(w3, a2) + b3) % p3
        a3_balanced = z3 % 2 
        return a1, a2, a3_balanced

    total_epochs = 30
    for epoch in range(1, total_epochs + 1):
        epoch_loss = 0
        
        # Keep track of layer weights before the updates in this epoch
        W1_old, W2_old, W3_old = W1.copy(), W2.copy(), W3.copy()
        
        for idx in range(len(raw_dataset)):
            raw_input = raw_dataset[idx]
            targets = target_dataset[idx]
            
            X_enc = np.array(encrypt_data(raw_input, pub_key))
            A1, A2, A3 = forward_pass(W1, W2, W3, X_enc)
            epoch_loss += np.sum((A3 - targets) ** 2)
            
            dW1 = compute_riemann_gradients_fast(W1, X_enc, b1, p1, targets, dx=1.0)
            dW2 = compute_riemann_gradients_fast(W2, A1, b2, p2, targets, dx=1.0)
            dW3 = compute_riemann_gradients_fast(W3, A2, b3, p3, targets, dx=1.0)
            
            W1 = move_prime_steps_fast(W1, dW1, prime_pool, step_slots=1)
            W2 = move_prime_steps_fast(W2, dW2, prime_pool, step_slots=1)
            W3 = move_prime_steps_fast(W3, dW3, prime_pool, step_slots=1)
            
        print(f"Epoch {epoch:02d}/{total_epochs} | Total Dataset Loss: {epoch_loss}")
        
        # Print a migration map at the first epoch, middle epoch, and final epoch
        if epoch == 1 or epoch == 15 or epoch == 30:
            print_weight_migration(W1_old, W1, f"LAYER 1 (Epoch {epoch})")
            
        if epoch_loss == 0:
            print(f"\nComplete Convergence achieved at Epoch {epoch}!")
            break

if __name__ == "__main__":
    train_network_on_dataset()
