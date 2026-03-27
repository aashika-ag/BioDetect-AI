from fastapi import FastAPI
from backend.app.api.routes import predict

app = FastAPI(title="BioDetect AI - HealthCare Track")

# Connect the prediction route
app.include_router(predict.router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "running", "engine": "active"}