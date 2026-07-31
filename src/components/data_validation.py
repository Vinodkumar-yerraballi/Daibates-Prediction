class DataValidation:
    REQUIRED_COLUMNS = [
        "gender", "age", "hypertension", "heart_disease", "smoking_history",
        "bmi", "HbA1c_level", "blood_glucose_level", "diabetes",
    ]

    def validate(self, data):
        missing_columns = [col for col in self.REQUIRED_COLUMNS if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing columns: {missing_columns}")
        if data.empty:
            raise ValueError("The dataset is empty")
        return data

    # Backward-compatible name used by earlier code.
    validation = validate
