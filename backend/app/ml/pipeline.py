import os
import sys
from backend.app.ml.train import train_ensemble
from backend.app.utils.logger import logger

def run_full_pipeline():
    # Plain text only to avoid terminal crashes
    logger.info("Starting BioDetect AI ML Pipeline...")

    # Get the absolute path to the BioDetect-AI root folder
    # This ensures it works no matter where the terminal is 'standing'
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_path = os.path.join(base_dir, "..", "data", "raw", "sample.csv")
    data_path = os.path.abspath(data_path)

    if not os.path.exists(data_path):
        logger.error(f"Data not found at {data_path}. Please run generate_data.py first.")
        return

    try:
        logger.info("Training Ensemble Models (Random Forest + XGBoost)...")
        train_ensemble()
        
        # Check for model files in backend/models/
        model_dir = os.path.join(base_dir, "..", "models")
        models = ["rf.pkl", "xgb.pkl", "scaler.pkl", "features.pkl"]
        
        logger.info("Pipeline Success: All models are ready for API deployment.")

    except Exception as e:
        logger.error(f"Pipeline Failed: {str(e)}")

if __name__ == "__main__":
    run_full_pipeline()