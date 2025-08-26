import streamlit as st
import joblib
import re
import string

# Load model & vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(f'[{string.punctuation}]', '', text)
    return text

# Streamlit UI
st.set_page_config(page_title="Email Spam Classifier", layout="centered")

st.title(" Email Spam Classifier")
st.write("Paste your email text below and check if it's spam or not.")

# Text input
email_text = st.text_area("Enter email content here...")

if st.button("Check"):
    if email_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        processed_text = preprocess_text(email_text)
        vectorized_text = vectorizer.transform([processed_text]).toarray()
        prediction = model.predict(vectorized_text)[0]

        if prediction == 1:
            st.error(" This email is SPAM!")
        else:
            st.success(" This email is NOT spam.")
