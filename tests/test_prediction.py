import pandas as pd

try:
    from src.pipelines.prediction_pipeline import Predictions
    from src.components.data_ingestion import DataIngestion
    from src.components.feature_enginering import build_preprocessor, prepare_training_data
except ImportError:
    from pipelines.prediction_pipeline import Predictions
    from components.data_ingestion import DataIngestion
    from components.feature_enginering import build_preprocessor, prepare_training_data


def test_build_preprocessor_transformer_structure():
    preprocessor = build_preprocessor()

    transformer_names = [name for name, _, _ in preprocessor.transformers]
    assert "numeric" in transformer_names
    assert "categorical" in transformer_names

    data = pd.DataFrame(
        [
            {
                "gender": "Female",
                "age": 30,
                "hypertension": 0,
                "heart_disease": 0,
                "smoking_history": "never",
                "bmi": 25.0,
                "HbA1c_level": 5.7,
                "blood_glucose_level": 120.0,
            }
        ]
    )

    output = preprocessor.fit_transform(data)
    assert output.shape[0] == 1


def test_prepare_training_data_uses_ingestion(monkeypatch):
    sample_data = pd.DataFrame(
        {
            "gender": ["Male", "Female"],
            "age": [30, 45],
            "hypertension": [0, 1],
            "heart_disease": [0, 0],
            "smoking_history": ["never", "current"],
            "bmi": [24.0, 29.0],
            "HbA1c_level": [5.6, 6.8],
            "blood_glucose_level": [110, 150],
            "diabetes": [0, 1],
        }
    )

    monkeypatch.setattr(DataIngestion, "load_data", lambda self: sample_data)
    x_train, x_test, y_train, y_test = prepare_training_data()

    assert "diabetes" not in x_train.columns
    assert y_train.name == "diabetes"


def test_predictions_returns_expected_values(monkeypatch):
    class DummyModel:
        def predict(self, frame):
            return [1]

        def predict_proba(self, frame):
            return [[0.1, 0.9]]

    monkeypatch.setattr("src.pipelines.prediction_pipeline.joblib.load", lambda path: DummyModel())
    prediction = Predictions(model_path="dummy.pkl")
    label, prob = prediction.predict(
        {
            "gender": "Male",
            "age": 50,
            "hypertension": 0,
            "heart_disease": 0,
            "smoking_history": "never",
            "bmi": 26.0,
            "HbA1c_level": 6.5,
            "blood_glucose_level": 130,
        }
    )

    assert label == 1
    assert prob == 0.9
