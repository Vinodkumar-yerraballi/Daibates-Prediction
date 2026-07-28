class DataValidation:
    def validation(self,data):
        columns=[
            "gender"
            ",age,"
            "hypertension,"
            "heart_disease,"
            "smoking_history,"
            "bmi,"
            "HbA1c_level,"
            "blood_glucose_level,"
            "diabetes"
        ]
        missing_columns=[col for col  in columns if col not in data.columns]
        if missing_columns:
            raise ValueError (
                f"Missing columns {missing_columns}"
            )
        if data.empty:
            raise ValueError (f"The data set error")
        return data