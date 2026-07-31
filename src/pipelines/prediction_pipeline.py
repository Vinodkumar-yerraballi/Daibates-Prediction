import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class Predictions:
    def __init__(self, model_path=None):
        root = Path(__file__).resolve().parents[2]
        self.model_path = Path(model_path or root / "artifacts" / "diabetes_model.pkl")
        self.model = joblib.load(self.model_path)

    def predict(self, data):
        frame = pd.DataFrame([data]) if isinstance(data, dict) else data.copy()
        prediction = self.model.predict(frame)
        prediction_prob = np.asarray(self.model.predict_proba(frame))[:, 1]
        return int(prediction[0]), float(prediction_prob[0])
