import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib
import os

MODEL_DIR = "models"

def preprocess(path):
    df = pd.read_csv(path)

    # Split features and target
    X = df.drop("target", axis=1)
    y = df["target"]

    # Handle missing values
    imputer = SimpleImputer(strategy="mean")
    X = imputer.fit_transform(X)

    # Normalize data
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Save artifacts
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(imputer, f"{MODEL_DIR}/imputer.pkl")
    joblib.dump(scaler, f"{MODEL_DIR}/scaler.pkl")

    return X, y