import numpy as np
from sieve import eratosthenes_sieve

def continuous_fermat_grid(Z_unmodulated, p, dx=0.1):
    """
    Computes Riemann integrals for an entire layer array simultaneously 
    by treating the matrix as an unrolled phase-shifted vector field.
    """
    scaled_z = Z_unmodulated.astype(float) / 100.0
    
    # Generate static fixed integration bounds
    lower_bound = 0.0
    upper_bound = 2 * np.pi
    steps = int((upper_bound - lower_bound) / dx)
    
    # Setup integration steps
    x_steps = lower_bound + np.arange(steps) * dx + (dx / 2.0)
    
    # Broadcast phase steps against scaled_z matrix layers
    # Resulting shape: (len(scaled_z), steps)
    phase_mesh = x_steps[None, :] + (scaled_z[:, None] / float(p))
    f_mesh = np.sin(phase_mesh) ** 2
    
    # Sum across the step dimension (axis=1) and scale by dx
    total_area = np.sum(f_mesh, axis=1) * dx
    return 1.0 / (1.0 + np.exp(-total_area + 3.0))

def compute_riemann_gradients_fast(W, X_enc, bias, p, targets, dx=1.0):
    """
    Fast parallelized finite difference gradient calculator.
    Perturbs individual neural connections rapidly across whole vector dimensions.
    """
    output_dim, input_dim = W.shape
    dW = np.zeros_like(W, dtype=float)
    
    def get_loss(current_W):
        raw_z = np.dot(current_W, X_enc) + bias
        preds = continuous_fermat_grid(raw_z, p)
        return np.sum((preds - targets) ** 2)

    base_loss = get_loss(W)
    
    # Test perturbations across weight coordinates
    for i in range(output_dim):
        for j in range(input_dim):
            W_perturbed = W.copy().astype(float)
            W_perturbed[i, j] += dx
            dW[i, j] = (get_loss(W_perturbed) - base_loss) / dx
            
    return dW

def move_prime_steps_fast(W, dW, prime_pool, step_slots=1):
    """Highly optimized directional projection into prime coordinates."""
    W_optimized = np.zeros_like(W, dtype=int)
    primes_arr = np.array(prime_pool)
    
    # Map raw gradient thresholds to active step changes (-1, 0, 1)
    signs = np.zeros_like(dW, dtype=int)
    signs[dW > 1e-7] = -1
    signs[dW < -1e-7] = 1
    
    for i in range(W.shape[0]):
        for j in range(W.shape[1]):
            # Find current index via fast absolute difference calculation
            pool_idx = np.abs(primes_arr - W[i, j]).argmin()
            new_idx = pool_idx + (signs[i, j] * step_slots)
            new_idx = max(0, min(new_idx, len(prime_pool) - 1))
            W_optimized[i, j] = prime_pool[new_idx]
            
    return W_optimized
