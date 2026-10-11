import numpy as np

def eratosthenes_sieve(limit=1000):
    """
    Generates a list of prime numbers up to a specified limit 
    using the historic Sieve of Eratosthenes algorithm.
    """
    # Create a boolean array "sieve" and initialize all entries it as True.
    # A value in sieve[i] will eventually become False if i is not a prime.
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[0:2] = False  # 0 and 1 are not prime numbers
    
    # Iterate through numbers up to the square root of the limit
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            # Mark all multiples of i starting from i*i as non-prime
            sieve[i*i::i] = False
            
    # Return the indices where the sieve array remains True
    return np.where(sieve)[0].tolist()

def initialize_prime_weights(input_dim, output_dim, prime_pool):
    """
    Constructs a weights matrix of size (output_dim, input_dim) 
    by drawing sequential prime numbers out of the generated pool.
    """
    if not prime_pool:
        raise ValueError("The prime pool cannot be empty.")
        
    weights = np.zeros((output_dim, input_dim), dtype=int)
    idx = 0
    
    # Populate the weight connections deterministically
    for i in range(output_dim):
        for j in range(input_dim):
            # Use modulo to wrap around if the pool size is smaller than the dimensions
            weights[i, j] = prime_pool[idx % len(prime_pool)]
            idx += 1
            
    return weights

# Simple execution block to verify the file works independently
if __name__ == "__main__":
    print("Testing Sieve of Eratosthenes...")
    sample_primes = eratosthenes_sieve(1000)
    print(f"Primes up to 1000: {sample_primes}")
    
    print("\nTesting Matrix Initialization (20x20)...")
    sample_matrix = initialize_prime_weights(20, 20, sample_primes)
    print("Generated Prime Weight Matrix:")
    print(sample_matrix)
