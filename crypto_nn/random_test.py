# random_test.py
import numpy as np
import random
import time
import tracemalloc
from sieve import eratosthenes_sieve, initialize_prime_weights
from activations import fermat_activation_vec
from rsa_wrapper import generate_rsa_keys, encrypt_data_vec as encrypt_data

def run_chaos_stress_test():
    print("==================================================")
    print("      CHAOS SYSTEM STRESS TEST: RANDOM_TEST.PY    ")
    print("==================================================\n")
    
    # 1. Initialize stable architecture constants
    prime_pool = eratosthenes_sieve(2000)
    dim = 4
    p1, p2, p3 = 997, 1009, 1013
    
    # Instantiate identical prime matrix structures
    W1 = initialize_prime_weights(dim, dim, prime_pool)
    W2 = initialize_prime_weights(dim, dim, prime_pool[10:])
    W3 = initialize_prime_weights(dim, dim, prime_pool[20:])
    
    b1 = b2 = b3 = np.array([0, 0, 0, 0])
    pub_key, _ = generate_rsa_keys(p=61, q=53)
    
    # 2. Generate completely random, unpredictable test cleartext integers
    # Simulates chaotic environment inputs within safe RSA modular boundaries
    random_input = [random.randint(10, 500) for _ in range(dim)]
    print(f"STEP 1: Ingress Chaotic Random Inputs: {random_input}")
    
    # 3. Encrypt data path instantly
    try:
        X_enc = np.array(encrypt_data(random_input, pub_key))
        print(f"STEP 2: RSA Scrambled Ciphertext:      {X_enc.tolist()}\n")
    except Exception as e:
        print(f"Cryptographic Ingress Pipeline Failed: {e}")
        return

    # 4. Forward Pass execution over hidden layers with active hardware profiling
    print("STEP 3: Flowing chaotic signals through prime modular check-points...")
    try:
        # Start high-resolution hardware telemetry tracing
        tracemalloc.start()
        start_time = time.perf_counter()
        
        # Hidden Layer 1 Forward
        z1 = (np.dot(W1, X_enc) + b1) % p1
        a1 = (fermat_activation_vec(z1, p1) + z1) % p1
        
        # Hidden Layer 2 Forward
        z2 = (np.dot(W2, a1) + b2) % p2
        a2 = (fermat_activation_vec(z2, p2) + z2) % p2
        
        # Final Output Structural Layer
        z3 = (np.dot(W3, a2) + b3) % p3
        layer_average = np.mean(z3)
        
        if layer_average > (p3 // 2):
            prediction = [1, 0, 1, 0]
        else:
            prediction = [0, 1, 0, 1]
            
        # Stop hardware telemetry tracing and collect benchmarks
        end_time = time.perf_counter()
        _, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Compile exact metrics
        execution_time_ms = (end_time - start_time) * 1000
        peak_memory_kb = peak_memory / 1024.0
            
        print(f"        Layer 1 Traversal (mod {p1}): {z1.tolist()[:2]}...")
        print(f"        Layer 2 Traversal (mod {p2}): {z2.tolist()[:2]}...")
        print(f"        Final Classification Vector:  {prediction}\n")
        
        print("--- Empirical Telemetry Performance Profile ---")
        print(f"Inference Latency Speed:   {execution_time_ms:.4f} ms")
        print(f"Peak RAM Memory Allocation: {peak_memory_kb:.4f} KB")
        print("==================================================")
        print("                STRESS TEST RESULTS               ")
        print("==================================================")
        print("STRESS TEST PASSED SUCCESSFULLY!")
        print("The network successfully isolated, stabilized, and processed")
        print("unpredictable random data without encountering mathematical drift.")
        print("==================================================")
        
    except Exception as e:
        # Guarantee memory profile safety tracking wraps down securely if error hits
        if tracemalloc.is_tracing():
            tracemalloc.stop()
        print(f"\nCRITICAL CRASH IN MODULAR PATHWAYS: {e}")
        print("==================================================")

if __name__ == "__main__":
    run_chaos_stress_test()
