import joblib
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from backend.app.ml.preprocess import prepare_data
import os

def train_ensemble():
    # Load and Split
    (X_train, X_test, y_train, y_test), scaler, feat_names = prepare_data()
    
    # 1. Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    
    # 2. XGBoost
    xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    xgb.fit(X_train, y_train)
    
    # Save models
    os.makedirs('models', exist_ok=True)
    joblib.dump(rf, 'models/rf.pkl')
    joblib.dump(xgb, 'models/xgb.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    joblib.dump(list(feat_names), 'models/features.pkl')
    
    print("✅ ML Engine: Models trained and saved to /models/")

if __name__ == "__main__":
    train_ensemble()