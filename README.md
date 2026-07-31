# Diabetes Prediction

## Project Overview

This repository contains a diabetes prediction project built with Python, scikit-learn, and pandas. It includes data ingestion, preprocessing, validation, model training, prediction, and test coverage for core components.

## Repository Structure

- `app.py` - application entrypoint (currently placeholder)
- `train.py` - training script entrypoint (currently placeholder)
- `requirements.txt` - dependency list for the project
- `setup.py` - package setup metadata
- `Dockerfile` - container build instructions
- `template.sh` - auxiliary shell script placeholder
- `artifacts/` - saved model artifact storage
- `data/` - dataset files used by the project
- `notebooks/` - exploratory Jupyter notebooks
- `src/` - main Python package containing project logic
- `tests/` - pytest test coverage for project components

### `src/` package

- `src/components/`
  - `data_ingestion.py` - reads the diabetes dataset CSV
  - `data_preprocessing.py` - cleans and fills missing numeric values
  - `data_transformation.py` - feature transformation logic (currently placeholder)
  - `data_validation.py` - checks required columns and dataset validity
  - `feature_enginering.py` - prediction wrapper around the saved model artifact
  - `model_evaluation.py` - model evaluation utilities (implementation may vary)
  - `model_trainer.py` - trains a scikit-learn pipeline with preprocessing and classifiers
- `src/pipelines/`
  - `training_pipeline.py` - preparation utilities for training workflows
  - `prediction_pipeline.py` - prediction wrapper and model inference logic

## Setup

1. Create or activate your Python environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

> Note: If your environment has compatibility issues with newer NumPy or pandas releases, consider using a Python virtual environment with compatible package versions.

## Dataset

The data file is located at:

- `data/diabetes_prediction_dataset.csv`

This dataset is expected to contain the following columns:

- `gender`
- `age`
- `hypertension`
- `heart_disease`
- `smoking_history`
- `bmi`
- `HbA1c_level`
- `blood_glucose_level`
- `diabetes`

## How to Use

### Run tests

Execute the test suite with pytest:

```bash
python -m pytest -q
```

### Model prediction

The prediction wrapper is implemented in `src/pipelines/prediction_pipeline.py`. It loads a saved `diabetes_model.pkl` artifact from the `artifacts/` folder and exposes a `Predictions` class.

Example usage:

```python
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root / 'src'))

from pipelines.prediction_pipeline import Predictions

predictor = Predictions()
input_data = {
    'gender': 'Male',
    'age': 54,
    'hypertension': 0,
    'heart_disease': 0,
    'smoking_history': 'never',
    'bmi': 28.5,
    'HbA1c_level': 6.1,
    'blood_glucose_level': 130,
}

label, probability = predictor.predict(input_data)
print('Predicted label:', label)
print('Probability:', probability)
```

### Training

Training logic is implemented in `src/components/model_trainer.py` and dataset preparation is available in `src/components/feature_enginering.py`. The top-level `train.py` script is currently a placeholder and can be extended to run the training pipeline end-to-end.

## Tests

Current tests are located in `tests/`:

- `tests/test_prediction.py` - prediction and pipeline integration tests
- `tests/test_transformation.py` - data preprocessing and validation tests

## Notes

- `app.py` and `train.py` are currently placeholders and may need implementation to support full app launch and model training workflows.
- The repository uses an artifact-based model file stored in `artifacts/diabetes_model.pkl`.

## Contact

For questions or updates, modify the repository files directly and run the test suite to verify behavior.
