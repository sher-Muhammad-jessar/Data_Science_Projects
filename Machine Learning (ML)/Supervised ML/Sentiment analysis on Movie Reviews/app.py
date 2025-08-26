import streamlit as st
import joblib

# Load model & vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# App title
st.title("🎬 Movie Review Sentiment Analysis")
st.write("Enter a movie review to see if it's Positive or Negative.")

# Text input
review = st.text_area("Review Text", "")

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review first.")
    else:
        # Transform & predict
        review_tfidf = vectorizer.transform([review])
        prediction = model.predict(review_tfidf)[0]
        probability = model.predict_proba(review_tfidf)[0][prediction]

        sentiment = "Positive 😀" if prediction == 1 else "Negative 😞"
        st.subheader(f"Prediction: {sentiment}")
        st.write(f"Confidence: {probability:.2%}")
