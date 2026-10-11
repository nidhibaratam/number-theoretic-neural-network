##  Example Execution Output

When you run `./run_all_tests.sh`, the terminal will execute the four-stage verification pipeline and output a detailed telemetry log. Here is an example of a successful run:

```text
==================================================
STARTING CRYPTO-NN AUTOMATED VERIFICATION SUITE
==================================================
Detected Environment: Mac/Linux Bash Execution Pipeline
Current Target Date: Sat Oct 10 19:43:48 IST 2026

=== STAGE 1: EXECUTING MATHEMATICAL UNIT TESTS ===
Testing Sieve Prime Weights Engine...
    -> sieve.py: PASS
Testing Vectorized Activations Tensor Layouts...
    -> activations.py: PASS
Testing Euclidean Algorithm Loss Metrics...
    -> loss.py: PASS
Testing RSA Cryptographic Modular Fields...
    -> rsa_wrapper.py: PASS

=== STAGE 2: EXECUTING SYSTEM INTEGRATION & TRAINING ===
Verifying Synthetic Production Dataset Density Maps...
    -> dataset_loader.py: PASS
Executing Macro Training Convergence Loop (Riemann Gradients)...
==================================================
    DEEP CRYPTO NN: VISUAL MIGRATION TRAINING LOOP
==================================================
Loaded 10 sample rows successfully.

Epoch 01/30 | Total Dataset Loss: 21

LAYER 1 (Epoch 1) WEIGHT MIGRATION MAP:
------------------------------------------------------------
[  2 •   2]   [  3 ▼   2]   [  5 ▼   2]   [  7 ▼   3]
[ 11 ▲  17]   [ 13 ▲  19]   [ 17 ▲  23]   [ 19 ▲  29]
[ 23 ▲  41]   [ 29 ▲  43]   [ 31 ▲  47]   [ 37 ▲  53]
[ 41 ▲  59]   [ 43 ▲  61]   [ 47 ▲  67]   [ 53 ▲  71]
------------------------------------------------------------
Epoch 02/30 | Total Dataset Loss: 22
...
Epoch 09/30 | Total Dataset Loss: 13
...
Epoch 30/30 | Total Dataset Loss: 17

LAYER 1 (Epoch 30) WEIGHT MIGRATION MAP:
------------------------------------------------------------
[  2 •   2]   [  2 •   2]   [  2 •   2]   [  2 •   2]
[ 17 •  17]   [ 19 •  19]   [ 23 •  23]   [ 29 •  29]
[ 41 •  41]   [ 43 •  43]   [ 47 •  47]   [ 53 •  53]
[ 59 •  59]   [ 61 •  61]   [ 67 •  67]   [ 71 •  71]
------------------------------------------------------------
    -> network.py: PASS

=== STAGE 3: EXECUTING RANDOM CHAOS STRESS TESTS ===
Testing Network Resilience against Chaos Noise Streams...
==================================================
      CHAOS SYSTEM STRESS TEST: RANDOM_TEST.PY    
==================================================

STEP 1: Ingress Chaotic Random Inputs: [227, 315, 250, 78]
STEP 2: RSA Scrambled Ciphertext:      [434, 2499, 1739, 3165]

STEP 3: Flowing chaotic signals through prime modular check-points...
        Layer 1 Traversal (mod 997): [332, 340]...
        Layer 2 Traversal (mod 1009): [523, 567]...
        Final Classification Vector:  [1, 0, 1, 0]

--- Empirical Telemetry Performance Profile ---
Inference Latency Speed:   0.3056 ms
Peak RAM Memory Allocation: 5.8770 KB
==================================================
                STRESS TEST RESULTS               
==================================================
STRESS TEST PASSED SUCCESSFULLY!
The network successfully isolated, stabilized, and processed
unpredictable random data without encountering mathematical drift.
==================================================
    -> random_test.py: PASS

=== STAGE 4: RUNNING DEPLOYMENT SUITE ===
Bundling pristine source assets into a release file...
==================================================
   ARCHIVING PARADIGM: CRYPTO-NN DISTRIBUTION
==================================================
Scanning project root for 10 verified components...
    Successfully packed: requirements.txt
    Successfully packed: sieve.py
    Successfully packed: activations.py
    Successfully packed: loss.py
    Successfully packed: rsa_wrapper.py
    Successfully packed: optimization.py
    Successfully packed: dataset_loader.py
    Successfully packed: network.py
    Successfully packed: plot_loss.py
    Successfully packed: prove_system.py

==================================================
              PACKAGING SUCCESSFUL                
==================================================
Your complete custom paradigm is archived inside:
    → crypto_nn_release_20261010_194350.zip
==================================================

==================================================
ALL SYSTEM INTEGRITY TESTS PASSED SUCCESSFULLY!
==================================================
