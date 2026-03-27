from pydantic import BaseModel
from typing import Dict, List

class PredictionResult(BaseModel):
    risk_score: float
    label: str  # e.g., "High Risk" or "Low Risk"
    explanation: Dict[str, float] # The SHAP values (Biomarker -> Impact)

class AnalyzeResponse(BaseModel):
    status: str
    patient_id: str
    data: PredictionResult
    recommendation: str