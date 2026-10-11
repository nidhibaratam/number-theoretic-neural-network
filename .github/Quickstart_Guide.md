## Quickstart Guide

Get the project up and running locally in under a minute with these simple steps.

### 1. Prerequisites
Ensure you have the following installed on your system:
* **Python 3.8 or higher**
* **Git**
* **Bash** (macOS/Linux terminal)

### 2. Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/nidhibaratam/number-theoretic-neural-network
cd number-theoretic-neural-network/crypto-nn
```
### 3. Set Up the Isolated Environment
Create and activate an isolated Python virtual environment, then install the required dependencies:

```bash
# Create virtual environment
python3 -m venv env

# Activate environment (macOS / Linux)
source env/bin/activate

# Install minimal dependencies
pip install -r requirements.txt
```

### 4. Run the Automated Verification Suite
Execute the master verification script to run all unit tests, macro training convergence loops, random chaos stress tests, and project packaging automatically:

#### For MacOS/Linux
```bash
chmod +x run_all_tests.sh
./run_all_tests.sh
```
#### For Windows
```bash
bash run_all_tests.sh
```
