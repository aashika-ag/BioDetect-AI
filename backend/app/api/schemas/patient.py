from pydantic import BaseModel, Field
from typing import Dict

class BloodPanel(BaseModel):
    # Field helps with documentation and validation
    albumin: float = Field(..., example=4.0)
    bilirubin: float = Field(..., example=0.6)
    creatinine: float = Field(..., example=0.9)

class GeneticMarkers(BaseModel):
    brca1: float = Field(..., example=5.2)
    tp53: float = Field(..., example=4.8)
    egfr: float = Field(..., example=7.1)

class Metabolomics(BaseModel):
    glucose: float = Field(..., example=5.5)
    lactate: float = Field(..., example=1.5)

class PatientRequest(BaseModel):
    """
    The main schema for the /analyze endpoint.
    This matches the structure expected by prediction_service.py
    """
    patient_id: str = Field(..., example="PATIENT_001")
    blood_panel: BloodPanel
    genetics: GeneticMarkers
    metabolomics: Metabolomics

    class Config:
        schema_extra = {
            "example": {
                "patient_id": "PATIENT_123",
                "blood_panel": {"albumin": 4.2, "bilirubin": 0.5, "creatinine": 0.8},
                "genetics": {"brca1": 6.1, "tp53": 3.9, "egfr": 8.0},
                "metabolomics": {"glucose": 5.2, "lactate": 1.2}
            }
        }