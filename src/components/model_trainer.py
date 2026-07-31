from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

try:
    from .feature_enginering import build_preprocessor, prepare_training_data
except ImportError:
    from src.components.feature_enginering import build_preprocessor, prepare_training_data


class ModelTrainer:
    def get_model(self):
        return {
            "LogisticRegression": LogisticRegression(max_iter=1000),
            "RandomForest": RandomForestClassifier(n_estimators=300, random_state=42),
        }

    def train_pipeline(self, model_name="LogisticRegression", data=None):
        model = self.get_model()[model_name]
        pipeline = Pipeline(
            [
                ("processor", build_preprocessor()),
                ("model", model),
            ]
        )
        x_train, _, y_train, _ = prepare_training_data(data)
        pipeline.fit(x_train, y_train)
        return pipeline
