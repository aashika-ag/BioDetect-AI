from fastapi import APIRouter, HTTPException
from backend.app.api.schemas.patient import PatientRequest
from backend.app.api.schemas.response import AnalyzeResponse
from backend.app.services.prediction_service import process_patient_request

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_patient(payload: PatientRequest):
    try:
        # 1. Process data through the ML Engine
        ml_result = process_patient_request(payload.dict())
        
        # 2. Determine clinical recommendation based on score
        rec = "Consult a specialist for diagnostic confirmation." if ml_result['risk_score'] > 0.7 else "Continue routine monitoring."
        
        # 3. Return the structured response
        return {
            "status": "success",
            "patient_id": payload.patient_id,
            "data": ml_result,
            "recommendation": rec
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference Error: {str(e)}")