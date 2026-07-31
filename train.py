from pathlib import Path

import joblib

from src.pipelines.training_pipeline import run_training_pipeline


if __name__ == "__main__":
    model = run_training_pipeline()
    path = Path("artifacts/diabetes_model.pkl")
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    print(f"Model saved to {path}")
