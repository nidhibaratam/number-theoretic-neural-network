#!/bin/bash
set -e

echo "=================================================="
echo -e "\033[1mSTARTING CRYPTO-NN AUTOMATED VERIFICATION SUITE\033[0m"
echo "=================================================="
echo "Detected Environment: Mac/Linux Bash Execution Pipeline"
echo -e "Current Target Date: $(date)\n"

# Check if the isolated virtual environment is active
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "Virtual environment (env) is not active in this terminal."
    echo "Attempting to locate and activate 'env/bin/activate' automatically..."
    if [ -f "env/bin/activate" ]; then
        source env/bin/activate
        echo -e "Isolated environment activated successfully.\n"
    else
        echo -e "ERROR: 'env/' folder not found. Please create your venv first.\n"
        exit 1
    fi
fi

# ------------------------------------------------------------
# STAGE 1: Standalone Mathematical Unit Tests
# ------------------------------------------------------------
echo "=== STAGE 1: EXECUTING MATHEMATICAL UNIT TESTS ==="
echo "Testing Sieve Prime Weights Engine..."
python3 sieve.py > /dev/null
echo "   -> sieve.py: PASS"

echo "Testing Vectorized Activations Tensor Layouts..."
python3 activations.py > /dev/null
echo "   -> activations.py: PASS"

echo "Testing Euclidean Algorithm Loss Metrics..."
python3 loss.py > /dev/null
echo "   -> loss.py: PASS"

echo "Testing RSA Cryptographic Modular Fields..."
python3 rsa_wrapper.py > /dev/null
echo -e "   -> rsa_wrapper.py: PASS\n"

# ------------------------------------------------------------
# STAGE 2: Core System & Optimization Stress Tests
# ------------------------------------------------------------
echo "=== STAGE 2: EXECUTING SYSTEM INTEGRATION & TRAINING ==="
echo "Verifying Synthetic Production Dataset Density Maps..."
python3 dataset_loader.py > /dev/null
echo "   -> dataset_loader.py: PASS"

echo "Executing Macro Training Convergence Loop (Riemann Gradients)..."
python3 network.py
echo -e "   -> network.py: PASS\n"

# ------------------------------------------------------------
# STAGE 3: Random Chaos Stress Tests
# ------------------------------------------------------------
echo "=== STAGE 3: EXECUTING RANDOM CHAOS STRESS TESTS ==="
echo "Testing Network Resilience against Chaos Noise Streams..."
# REMOVED "> /dev/null" to let the script print its outputs directly
python3 random_test.py
echo -e "   -> random_test.py: PASS\n"


# ------------------------------------------------------------
# STAGE 4: Final Production Packaging
# ------------------------------------------------------------
echo "=== STAGE 4: RUNNING DEPLOYMENT SUITE ==="
echo "Bundling pristine source assets into a release file..."
python3 bundle_project.py

echo -e "\n=================================================="
echo -e "\033[1;32mALL SYSTEM INTEGRITY TESTS PASSED SUCCESSFULLY!\033[0m"
echo "=================================================="
