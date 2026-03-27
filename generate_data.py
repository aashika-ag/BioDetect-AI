import pandas as pd
import numpy as np
import os

def generate_medical_data(n_samples=200):
    np.random.seed(42)
    
    data = {
        'patient_id': [f"PATIENT_{i:03d}" for i in range(n_samples)],
        
        # Blood Panel (e.g., Protein levels)
        'albumin_g_dL': np.random.normal(4.0, 0.5, n_samples),
        'bilirubin_mg_dL': np.random.normal(0.6, 0.3, n_samples),
        'creatinine_mg_dL': np.random.normal(0.9, 0.2, n_samples),
        
        # Gene Expression (Normalized RNA-seq values)
        'gene_BRCA1': np.random.uniform(0, 10, n_samples),
        'gene_TP53': np.random.uniform(0, 10, n_samples),
        'gene_EGFR': np.random.uniform(0, 10, n_samples),
        
        # Metabolomics (Small molecules)
        'glucose_mmol_L': np.random.normal(5.5, 1.2, n_samples),
        'lactate_mmol_L': np.random.normal(1.5, 0.5, n_samples),
        
        # Target: 1 (Disease Detected), 0 (Healthy)
        'target': np.random.choice([0, 1], size=n_samples, p=[0.7, 0.3])
    }
    
    df = pd.DataFrame(data)
    
    # Create the directory if it doesn't exist
    os.makedirs('data/raw', exist_ok=True)
    
    # Save to the path expected by your train.py
    df.to_csv('data/raw/sample.csv', index=False)
    print(f"✅ Success! Created 'data/raw/sample.csv' with {n_samples} patient records.")

if __name__ == "__main__":
    generate_medical_data()