from app.ml.train import train_ensemble
import os

print("--- Starting BioDetect AI ML Pipeline ---")

if not os.path.exists('data/raw/sample.csv'):
    print("❌ Error: data/raw/sample.csv not found. Run generate_data.py first!")
else:
    train_ensemble()
    print("--- Pipeline Complete: System is ready for API Deployment ---")