from fastapi import APIRouter
import joblib
import os

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Checks the status of the API and verifies that ML models are present.
    """
    # Check if model files exist
    model_path = "backend/models/"
    required_models = ["rf.pkl", "xgb.pkl", "scaler.pkl"]
    
    missing_models = [m for m in required_models if not os.path.exists(os.path.join(model_path, m))]
    
    status = "healthy" if not missing_models else "degraded"
    
    return {
        "status": status,
        "version": "1.0.0",
        "track": "HealthCare",
        "system": "BioDetect AI",
        "checks": {
            "api_layer": "online",
            "ml_models": "loaded" if status == "healthy" else f"missing: {missing_models}",
            "device": "CPU" # Can be updated to CUDA if using GPU
        }
    }