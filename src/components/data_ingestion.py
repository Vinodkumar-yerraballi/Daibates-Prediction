import pandas as pd

class DataIngestion:
    def __init__(self):
        self.data_path='data/diabetes_prediction_dataset.csv'

    def load_data(self):
        data=pd.read_csv(self.data_path)
        return data