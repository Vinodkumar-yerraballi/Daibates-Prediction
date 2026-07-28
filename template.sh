# Create a folders
mkdir -p data
mkdir -p notebooks
mkdir -p src
mkdir -p src/components
mkdir -p src/pipelines
mkdir -p artifacts
mkdir -p tests

# in the folder create files
touch src/__init__.py
touch src/exception.py
touch src/logger.py
touch src/utils.py
touch src/components/__init__.py
touch src/components/data_ingestion.py
touch src/components/data_transformation.py
touch src/components/model_trainer.py
touch src/components/model_evaluation.py
touch src/pipelines/__init__.py
touch src/pipelines/training_pipeline.py
touch src/pipelines/prediction_pipeline.py
touch tests/test_transformation.py
touch tests/test_prediction.py
touch app.py
touch train.py
touch requirements.txt
touch setup.py
touch Dockerfile
touch README.md