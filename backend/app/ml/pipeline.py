from app.ml.preprocess import preprocess

if __name__ == "__main__":
    X, y = preprocess("data/raw/sample.csv")
    print("Preprocessing done ✅")
    print("Shape:", X.shape)