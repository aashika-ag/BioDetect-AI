import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def prepare_data(filepath="data/raw/sample.csv"):
    df = pd.read_csv(filepath)
    
    # Separate ID and Target
    X = df.drop(columns=['target', 'patient_id'])
    y = df['target']
    
    # Normalize data (StandardScaler)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42), scaler, X.columns

def get_top_features(model, feature_names, n=5):
    """Returns the most important biomarkers identified by the AI"""
    importances = model.feature_importances_
    indices = np.argsort(importances)[-n:]
    return [feature_names[i] for i in indices]