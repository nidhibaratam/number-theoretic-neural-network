import os
import zipfile
from datetime import datetime

def package_crypto_nn():
    print("==================================================")
    print("   ARCHIVING PARADIGM: CRYPTO-NN DISTRIBUTION")
    print("==================================================")
    
    # 1. Target codebase modules to include in the release archive
    required_files = [
        "requirements.txt",
        "sieve.py",
        "activations.py",
        "loss.py",
        "rsa_wrapper.py",
        "optimization.py",
        "dataset_loader.py",
        "network.py",
        "plot_loss.py",
        "prove_system.py"
    ]
    
    # Generate a professional timestamped archive filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"crypto_nn_release_{timestamp}.zip"
    
    print(f"Scanning project root for {len(required_files)} verified components...")
    
    missing_files = [f for f in required_files if not os.path.exists(f)]
    if missing_files:
        print(f"\n WARNING: The following files were not found and will be skipped: {missing_files}")
    
    # 2. Compile files into a structured zip format
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in required_files:
                if os.path.exists(file):
                    # Add file to the archive structure cleanly
                    zipf.write(file)
                    print(f"   Successfully packed: {file}")
            
            # Optional: Check if a saved image graph exists to bundle it in
            if os.path.exists("image_qgovDl.png"):
                zipf.write("image_qgovDl.png", arcname="optimization_proof_graph.png")
                print("   Successfully packed: optimization_proof_graph.png")
                
        print("\n==================================================")
        print("               PACKAGING SUCCESSFUL               ")
        print("==================================================")
        print(f"Your complete custom paradigm is archived inside:\n   → {zip_filename}")
        print("==================================================")
        
    except Exception as e:
        print(f"\nError encountered during compression phase: {e}")

if __name__ == "__main__":
    package_crypto_nn()
