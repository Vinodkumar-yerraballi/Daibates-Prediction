from sklearn.metrics import accuracy_score,f1_score,roc_auc_score,precision_score,recall_score
import joblib
from pathlib import Path

from src.components.model_trainer import ModelTrainer

def model_metric(model, x_test, y_test):
    prediction = model.predict(x_test)
    prediction_prob = model.predict_proba(x_test)[:, 1]
    return {
        "accuracy_score": accuracy_score(y_test, prediction),
        "f1_score": f1_score(y_test, prediction),
        "precision": precision_score(y_test, prediction, zero_division=0),
        "recall_score": recall_score(y_test, prediction, zero_division=0),
        "roc_auc_score": roc_auc_score(y_test, prediction_prob),
    }

def train_and_save_model(model_path=None):
    model_path = Path(model_path or "artifacts/diabetes_model.pkl")
    model_path.parent.mkdir(parents=True, exist_ok=True)
    pipeline = ModelTrainer().train_pipeline()
    joblib.dump(pipeline, model_path)
    return pipeline


if __name__ == "__main__":
    train_and_save_model()
