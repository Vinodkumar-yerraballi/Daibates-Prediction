from sklearn.metrics import accuracy_score,f1_score,roc_auc_score,precision_score,recall_score
import joblib
from src.components.model_trainer import ModelTrainer

def model_metric(model,x_test,y_test):
    prediction=model.fit(x_test)
    prediction_prob=model.predict_prod(x_test)[:,1]
    return {
        "accuracy_score":accuracy_score(y_test,prediction),
        "f1_score":f1_score(y_test,prediction),
        "precision":precision_score(y_test.prediction),
        "recall_score":recall_score(y_test,prediction),
        "roc_auc_score":roc_auc_score(y_test,prediction_prob)
    }

model_trainer= ModelTrainer()
pipeline = model_trainer.train_pipeline()
joblib.dump(
    pipeline,"models/diabetes_model.pkl"
)