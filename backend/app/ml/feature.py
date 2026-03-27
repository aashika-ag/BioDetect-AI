from sklearn.ensemble import ExtraTreesClassifier
import pandas as pd

def get_top_features(X, y, n=10):
    model = ExtraTreesClassifier()
    model.fit(X, y)
    # Returns the indices of the most important biomarkers
    return model.feature_importances_.argsort()[-n:][::-1]