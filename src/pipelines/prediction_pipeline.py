import joblib
import pandas as pd

class Predictions:
    def __init__(self):
        self.model=joblib.load("models/diabetes_model.pkl")
    def predict(self,data):
        data=pd.DataFrame([data])
        prediction=self.predict(data)
        prediction_prob=self.predict_prob(data)[:,1]
        return prediction[0] ,prediction_prob[0]