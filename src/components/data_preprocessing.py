import numpy as np

class DataPreprocessing:
    def data_processor(self,data):
        data=data.copy()
        data.drop_duplicates(inplace=True)

        columns=[
            "bmi,"
            "HbA1c_level",
            "blood_glucose_level"
        ]
        for col in columns:
            data[col]=data[col].fillna(0,np.nan)
        return data
