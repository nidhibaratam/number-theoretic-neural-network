import math
from sympy import invert
import numpy as np

def generate_rsa_keys(p=61, q=53):
    """
    Generates standard RSA public and private key pairs.
    Uses moderate primes for local validation, but handles large data paths.
    """
    if p == q:
        raise ValueError("Primes p and q must be distinct.")
        
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose a standard public exponent coprime to phi
    e = 65537
    if math.gcd(e, phi) != 1:
        # Fallback to a smaller prime if standard fails validation boundaries
        e = 17
        while math.gcd(e, phi) != 1:
            e += 2
            
    # Compute private exponent d using SymPy's efficient modular inverse
    d = int(invert(e, phi))
    
    return (e, n), (d, n)


def encrypt_data_vec(data, public_key):
    """Vectorized RSA Encryption using NumPy array mapping."""
    e, n = public_key
    data_arr = np.array(data, dtype=int)
    
    if np.any(data_arr >= n):
        bad_val = data_arr[data_arr >= n][0]
        raise ValueError(f"Data value {bad_val} is too large for RSA modulus {n}.")
        
    # Vectorized element-wise fast modular exponentiation
    encrypt_func = np.vectorize(lambda m: pow(int(m), e, n))
    return encrypt_func(data_arr).tolist()

def decrypt_data_vec(cipher, private_key):
    """Vectorized RSA Decryption using NumPy array mapping."""
    d, n = private_key
    cipher_arr = np.array(cipher, dtype=int)
    
    decrypt_func = np.vectorize(lambda c: pow(int(c), d, n))
    return decrypt_func(cipher_arr).tolist()


# rsa_wrapper.py (Bottom Execution Block Update)
if __name__ == "__main__":
    print("Testing RSA Cryptographic Shield Layer...")
    
    # Add function aliases so the standalone test block matches your updated vector names perfectly
    encrypt_data = encrypt_data_vec
    decrypt_data = decrypt_data_vec
    
    # Generate corporate testing keypairs
    pub_key, priv_key = generate_rsa_keys()
    print(f"Public Cryptographic Key (e, n): {pub_key}")
    print(f"Private Decryption Key (d, n): {priv_key}")
    
    # Target numeric payload simulation
    sample_cleartext = [42, 105, 7]
    print(f"\nOriginal Input Elements: {sample_cleartext}")
    
    cipher_output = encrypt_data(sample_cleartext, pub_key)
    print(f"Encrypted Safe Primitives: {cipher_output}")
    
    decrypted_verify = decrypt_data(cipher_output, priv_key)
    print(f"Decrypted Elements Verification: {decrypted_verify}")

