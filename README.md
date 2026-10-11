# Discrete Number-Theoretic Neural Network Architecture via Modular Primitives

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Verification Status](https://img.shields.io/badge/Telemetry-100%25%20Passed-brightgreen.svg)](#automated-telemetry--verification-suite)


---

##  Overview

Conventional deep learning relies heavily on continuous floating-point representations ($\mathbb{R}^{m \times n}$) and backpropagation, incurring massive compute and memory overhead on resource-constrained platforms. 

This repository implements a **discrete, integer-only number-theoretic neural network** that operates entirely over finite modular arithmetic primitives:
1. **Prime Weight Initialization:** Deterministic matrix generation via the **Sieve of Eratosthenes**.
2. **Modular Non-Linear Activations:** Vectorized transformations using **Fermat's Little Theorem** and **Wilson's Theorem** residue scalings.
3. **Algebraic Loss Metrics:** Model divergence evaluated via the **Euclidean Greatest Common Divisor (GCD) Algorithm**.
4. **Discrete Parameter Optimization:** Multi-directional parameter update routing via **Riemann Finite-Difference Gradients**.
5. **Cryptographic Input Conditioning:** Native modular exponentiation shield via **RSA Public-Key Exponentiation Rings**.

---

## Empirical Telemetry Benchmarks

Validated via dynamic heap profiling (`tracemalloc`) and high-resolution performance timers (`time.perf_counter`):

| Performance Metric | Measured Value | Operational Status / Constraint |
| :--- | :---: | :---: |
| **Inference Latency** | **0.3056 ms** | Optimal Real-Time Forward Pass |
| **Peak RAM Footprint** | **5.8770 KB** | Ultra-Constraint Edge Hardware Safe |
| **Chaos Resilience** | **Passed (0 Drift)** | Zero Mathematical Overflow under RSA Noise |
| **Dataset Convergence** | **30 Epochs** | Stable Discrete Attractor Lock |

---

##  Repository File Architecture

```text
crypto_nn/
├── activations.py      # Vectorized Fermat & Wilson modular activation functions
├── dataset_loader.py   # Synthetic prime-density classification data pipeline
├── loss.py             # Euclidean GCD distance metric calculation
├── network.py          # Macro architecture forward pass & Riemann gradient loops
├── optimization.py     # Directional prime coordinate parameter projection
├── plot_loss.py        # Matplotlib visualization engine for loss trajectory
├── prove_system.py     # Deterministic single-sample mathematical proof test
├── random_test.py     # Chaos stress test suite & real-time telemetry tracer
├── rsa_wrapper.py      # Vectorized RSA public-key modular exponentiation shield
├── run_all_tests.sh    # Automated 4-stage system validation & test suite
├── sieve.py            # Deterministic Sieve of Eratosthenes prime pool generator
├── bundle_project.py   # Release packaging and asset verification script
├── requirements.txt    # Minimal environment dependencies
├── references.bib      # Synchronized BibTeX bibliography
└── Visual proof.png    # High-resolution Riemann loss convergence plot


```
---

## Documentation
- [Quickstart Guide](./Quickstart_Guide.md)
- [Example Output](./Example_output.md)
---
