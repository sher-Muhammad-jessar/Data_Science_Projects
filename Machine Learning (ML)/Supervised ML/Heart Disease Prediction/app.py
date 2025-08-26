import streamlit as st
import joblib
import numpy as np

# Load model and scaler 
model = joblib.load("Heart_Disease_model.pkl")
scaler = joblib.load("Scaler.pkl")

st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="centered")
st.title("❤️ Heart Disease Prediction")
st.write("Enter your heart details to check your risk:")

# Input fields
age = st.number_input("Age", 20, 100, 50)
sex = st.selectbox("Sex", ["Female", "Male"])
cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
chol = st.number_input("Cholesterol", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG (0–2)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", 60, 250, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression", 0.0, 10.0, 1.0)
slope = st.selectbox("Slope of ST Segment", [0, 1, 2])
ca = st.selectbox("Major Vessels (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (1–3)", [1, 2, 3])

if st.button("Predict"):
    # Convert input to array
    input_data = np.array([[age, 1 if sex == "Male" else 0, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    
    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1]

    if prediction == 1:
        st.error(f"🚨 HIGH risk of Heart Disease ({prob*100:.2f}% probability)")
    else:
        st.success(f"✅ Low risk of Heart Disease ({prob*100:.2f}% probability)")
