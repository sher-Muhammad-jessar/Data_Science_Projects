import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline (preprocessing + model)
model = joblib.load("bike_model.pkl")

st.title("🚲 Bike Rental Demand Prediction")

# User Inputs
season = st.selectbox("Season", [1, 2, 3, 4])  # 1:Spring, 2:Summer, 3:Fall, 4:Winter
mnth = st.selectbox("Month", list(range(1, 13)))
hr = st.selectbox("Hour of Day", list(range(0, 24)))
weekday = st.selectbox("Weekday (0=Sunday)", list(range(0, 7)))
weathersit = st.selectbox("Weather Situation", [1, 2, 3, 4])
holiday = st.selectbox("Holiday", [0, 1])
workingday = st.selectbox("Working Day", [0, 1])
temp = st.slider("Temperature (normalized)", 0.0, 1.0, 0.5)
hum = st.slider("Humidity (normalized)", 0.0, 1.0, 0.5)
windspeed = st.slider("Windspeed (normalized)", 0.0, 1.0, 0.2)

# Create DataFrame for prediction
input_df = pd.DataFrame({
    "season": [season],
    "mnth": [mnth],
    "hr": [hr],
    "weekday": [weekday],
    "weathersit": [weathersit],
    "holiday": [holiday],
    "workingday": [workingday],
    "temp": [temp],
    "hum": [hum],
    "windspeed": [windspeed]
})

# Predict
if st.button("Predict Rentals"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Rentals: {int(prediction[0])} bikes")
