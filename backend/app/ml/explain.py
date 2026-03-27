import shap
import joblib

def get_explanation(model_path, data_row):
    model = joblib.load(model_path)
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(data_row)
    return shap_values