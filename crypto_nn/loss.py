import math

def euclidean_loss(predictions, targets):
    """
    Evaluates network performance using the Greatest Common Divisor (GCD).
    
    Instead of calculating a traditional geometric distance, this measures 
    the structural number-theoretic discrepancy between predictions and targets.
    A lower loss value indicates a stronger common factor profile.
    """
    if len(predictions) != len(targets):
        raise ValueError("Dimensions of predictions and targets must match.")
        
    total_loss = 0
    for pred, target in zip(predictions, targets):
        p_val = int(pred)
        t_val = int(target)
        
        # Calculate the Greatest Common Divisor using the Euclidean Algorithm
        gcd_val = math.gcd(p_val, t_val)
        
        # Loss Metric: Measures how far the shared divisor is from the target identity.
        # If prediction == target, gcd(target, target) == target, making the loss 0.
        total_loss += abs(t_val - gcd_val)
        
    return total_loss

# Simple execution block to verify the loss logic independently
if __name__ == "__main__":
    print("Testing Euclidean Algorithm Loss...")
    
    # Example 1: Perfect Match
    sample_preds_1 = [5, 12, 7]
    sample_targets_1 = [5, 12, 7]
    loss_1 = euclidean_loss(sample_preds_1, sample_targets_1)
    print(f"Loss with perfect targets {sample_targets_1}: {loss_1} (Expect 0)")
    
    # Example 2: Deviated Match
    sample_preds_2 = [1, 0, 1]  # Imagine output from your Fermat layer
    sample_targets_2 = [3, 5, 2]
    loss_2 = euclidean_loss(sample_preds_2, sample_targets_2)
    print(f"Loss with Fermat outputs {sample_preds_2} vs Targets {sample_targets_2}: {loss_2}")
