import pandas as pd
import pytest

from src.components.data_preprocessing import DataPreprocessing
from src.components.data_validation import DataValidation


def test_preprocessing_removes_duplicates_and_fills_numeric_values():
    data = pd.DataFrame({"bmi": [None, None], "HbA1c_level": [6.1, 6.1], "blood_glucose_level": [120, 120]})
    result = DataPreprocessing().data_processor(data)
    assert len(result) == 1
    assert result["bmi"].iloc[0] == 0


def test_validation_reports_missing_columns():
    with pytest.raises(ValueError, match="Missing columns"):
        DataValidation().validate(pd.DataFrame())
