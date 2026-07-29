from pathlib import Path

import pandas as pd


class DataIngestion:
    def __init__(self):
        project_root = Path(__file__).resolve().parents[2]
        self.data_path = project_root / "data" / "diabetes_prediction_dataset.csv"

    def load_data(self):
        data = pd.read_csv(self.data_path)
        return data