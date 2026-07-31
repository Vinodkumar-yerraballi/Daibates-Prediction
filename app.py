import streamlit as st
from src.pipelines.prediction_pipeline import Predictions

st.title("Diabetes Prediction System")


gender=st.radio("Select Gender",["Male","Female"])
if gender=="Male":
    gender =1
else:
    gender =0
age=st.number_input("age",value=10)
smoking_history=st.radio("Select Smoking_status",['No Info', 'current', 'ever', 'former', 'never', 'not current'}])
if smoking_history=="No info":
    smoking_history=0
elif smoking_history=="current":
    smoking_history=1
elif smoking_history=="ever":
    smoking_history=3
elif smoking_history=="former":
    smoking_history=4
elif smoking_history=="never":
    smoking_history=5
else:
    smoking_history=6
hypertension=st.radio("Select Hypertension",["Yes","No"])
if hypertension=="Yes":
    hypertension=1
else:
    hypertension=0
heart_disease=st.radio("Select Heart_disease",["Yes","No"])
if heart_disease=="Yes":
    heart_disease=1
else:
    heart_disease=0
bmi=st.slider("Body mass induction",min_value=10,max_value=95)
HbA1c_level=st.slider("Body mass induction",min_value=3,max_value=9)
blood_glucose_level=st.slider("blood_glucose_level",min_value=80,max_value=300)
if st.button("Predict"):
    data={
        'gender':gender,
        "age":age,
        "smoking_history":smoking_history,
        'hypertension':hypertension,
        "heart_disease":heart_disease,
        "bmi":bmi,
        "HbA1c_level":HbA1c_level,
        "blood_glucose_level":blood_glucose_level

    }

    pipeline=Predictions()

    Predictions, probability=pipeline.predict(data)

    if Predictions==1:
        st.error("High Risk of Diabetes")
    else:
        st.success("Low risk Diabetes")
    st.write(f"Probability: {probability:.2%}")

