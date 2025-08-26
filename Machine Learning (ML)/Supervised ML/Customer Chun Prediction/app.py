import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("churn_model.pkl")

# App title
st.title("📊 Telco Customer Churn Prediction")
st.write("Enter customer details to predict the likelihood of churn.")

# Input form
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=2000.0)

# Convert input to DataFrame
input_data = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [senior],
    'Partner': [partner],
    'Dependents': [dependents],
    'tenure': [tenure],
    'PhoneService': [phone_service],
    'MultipleLines': [multiple_lines],
    'InternetService': [internet_service],
    'OnlineSecurity': [online_security],
    'OnlineBackup': [online_backup],
    'DeviceProtection': [device_protection],
    'TechSupport': [tech_support],
    'StreamingTV': [streaming_tv],
    'StreamingMovies': [streaming_movies],
    'Contract': [contract],
    'PaperlessBilling': [paperless_billing],
    'PaymentMethod': [payment_method],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges]
})

# Predict button
if st.button("Predict Churn"):
    # Prediction
    prob = model.predict_proba(input_data)[:, 1][0]
    pred = "Yes" if prob >= 0.5 else "No"

    st.subheader(f"Prediction: {pred}")
    st.write(f"**Churn Probability:** {prob:.2%}")

    # SHAP Explanation
    st.subheader("Feature Importance (SHAP Values)")

    # Extract trained RF and preprocessing
    explainer = shap.TreeExplainer(model.named_steps['rf'])
    X_transformed = model.named_steps['prep'].transform(input_data)

    shap_values = explainer.shap_values(X_transformed)

    # Handle different SHAP output formats
    if isinstance(shap_values, list) and len(shap_values) > 1:
        shap_data = shap_values[1]  # Positive class
    else:
        shap_data = shap_values  # Already single output

    # Global summary plot (for the single prediction it's more like local importance)
    fig, ax = plt.subplots()
    shap.summary_plot(shap_data, X_transformed, feature_names=explainer.feature_names, show=False)
    st.pyplot(fig)
