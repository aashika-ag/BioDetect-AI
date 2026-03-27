import joblib
import numpy as np
from backend.app.ml.predict import get_prediction_logic

def process_patient_request(data_dict: dict):
    # This matches the order of features in your generate_data.py: 
    # [3 blood, 3 genes, 2 metabolites]
    input_values = [
        data_dict['blood_panel']['albumin'],
        data_dict['blood_panel']['bilirubin'],
        data_dict['blood_panel']['creatinine'],
        data_dict['genetics']['brca1'],
        data_dict['genetics']['tp53'],
        data_dict['genetics']['egfr'],
        data_dict['metabolomics']['glucose'],
        data_dict['metabolomics']['lactate']
    ]
    
    # Run the ML logic we wrote in Part 1
    result = get_prediction_logic(input_values)
    return result