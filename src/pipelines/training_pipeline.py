from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import DataPreprocessing
from src.components.data_validation import DataValidation
from src.components.model_trainer import ModelTrainer


def run_training_pipeline():
    data = DataIngestion().load_data()
    data = DataValidation().validate(data)
    data = DataPreprocessing().data_processor(data)
    return ModelTrainer().train_pipeline(data=data)
