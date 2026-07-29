from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

try:
    from .data_ingestion import DataIngestion
except ImportError:
    from src.components.data_ingestion import DataIngestion


class FeatureEngineer:
    def transform(self, data):
        data = data.copy()
        return data


def prepare_training_data():
    data_loader = DataIngestion()
    data = data_loader.load_data()
    x = data.drop("diabetes", axis=1)
    y = data["diabetes"]
    return train_test_split(x, y, test_size=0.20, random_state=42)


x_train, x_test, y_train, y_test = prepare_training_data()

processor = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)