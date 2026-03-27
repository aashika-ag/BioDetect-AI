import joblib
import numpy as np
import shap

def get_prediction_logic(input_data: list):
    """
    input_data: A flat list of all numerical values from the blood/gene/metabolomics panel
    """
    # Load artifacts
    rf = joblib.load('models/rf.pkl')
    xgb = joblib.load('models/xgb.pkl')
    scaler = joblib.load('models/scaler.pkl')
    features = joblib.load('models/features.pkl')

    # Prep Input
    data_array = np.array([input_data])
    scaled_data = scaler.transform(data_array)

    # Ensemble Prediction (Average of RF and XGBoost)
    rf_prob = rf.predict_proba(scaled_data)[0][1]
    xgb_prob = xgb.predict_proba(scaled_data)[0][1]
    final_risk = (rf_prob + xgb_prob) / 2

    # SHAP Explainability (Why did the AI say this?)
    explainer = shap.TreeExplainer(rf)
    shap_values = explainer.shap_values(scaled_data)
    
    # Map SHAP values to feature names for the frontend
    # If it's a binary classification, shap_values is a list; we take the positive class [1]
    explanation = {features[i]: float(shap_values[1][0][i]) for i in range(len(features))}

    return {
        "risk_score": round(float(final_risk), 4),
        "explanation": explanation,
        "label": "High Risk" if final_risk > 0.7 else "Low Risk"
    }