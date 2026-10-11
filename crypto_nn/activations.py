import numpy as np
import math

def fermat_activation_vec(Z, p):
    """
    Vectorized implementation of Fermat's Little Theorem.
    Flattens computing time by running element-wise modular operations natively.
    """
    # Fast element-wise evaluation wrapper
    func = np.vectorize(lambda z: pow(int(z), p - 1, p) if math.gcd(int(z), p) == 1 else 0)
    return func(Z)

def wilson_activation_vec(Z, p):
    """
    Vectorized Wilson's Theorem Activation.
    Scales the entire matrix by the factorial residue in a single operation.
    """
    wilson_constant = math.factorial(p - 1) % p
    return (Z.astype(int) * wilson_constant) % p


# Simple execution block to verify the activations independently
if __name__ == "__main__":
    print("Testing Activations with Layer Prime Modulus p = 7...")
    test_signals = [3, 14, 5]  # Note: 14 shares a factor with 7 (gcd(14,7) = 7)
    print(f"Input Signals: {test_signals}")
    
    fermat_out = fermat_activation_vec(np.array(test_signals), 7)
    print(f"Fermat's Little Theorem Activation (Should be binary): {fermat_out}")
    
    wilson_out = wilson_activation_vec(np.array(test_signals), 7)
    print(f"Wilson's Theorem Activation (Factorial Modular Scaling): {wilson_out}")
