import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("Linaer_model.pkl")

st.set_page_config(page_title="Startup Profit Predictor", page_icon="💰", layout="centered")
st.title("💰 Startup Profit Prediction")
st.write("Enter startup spending details to estimate profit.")

# Input fields
rd_spend = st.number_input("R&D Spend ($)", min_value=0.0, value=50000.0)
admin_spend = st.number_input("Administration Spend ($)", min_value=0.0, value=20000.0)
marketing_spend = st.number_input("Marketing Spend ($)", min_value=0.0, value=30000.0)
state = st.selectbox("State", ["New York", "California", "Florida"])

# Predict
if st.button("Predict Profit"):
    # Create DataFrame for input
    input_df = pd.DataFrame({
        "State": [state],
        "R&D Spend": [rd_spend],
        "Administration": [admin_spend],
        "Marketing Spend": [marketing_spend]
    })

    prediction = model.predict(input_df)[0]
    st.success(f"💵 Estimated Profit: ${prediction:,.2f}")
