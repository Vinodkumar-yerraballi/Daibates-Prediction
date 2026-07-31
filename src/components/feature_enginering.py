from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

try:
    from .data_ingestion import DataIngestion
except ImportError:
    from src.components.data_ingestion import DataIngestion


NUMERIC_FEATURES = ["age", "hypertension", "heart_disease", "bmi", "HbA1c_level", "blood_glucose_level"]
CATEGORICAL_FEATURES = ["gender", "smoking_history"]


def prepare_training_data(data=None):
    if data is None:
        data = DataIngestion().load_data()
    x = data.drop("diabetes", axis=1)
    y = data["diabetes"]
    return train_test_split(x, y, test_size=0.20, random_state=42)


x_train, x_test, y_train, y_test = prepare_training_data()

def build_preprocessor():
    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])
    return ColumnTransformer([
        ("numeric", numeric_pipeline, NUMERIC_FEATURES),
        ("categorical", categorical_pipeline, CATEGORICAL_FEATURES),
    ])
