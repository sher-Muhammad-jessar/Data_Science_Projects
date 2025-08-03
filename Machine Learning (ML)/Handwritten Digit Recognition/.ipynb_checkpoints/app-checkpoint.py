import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import cv2
import joblib

# Load trained model
model = joblib.load("knn_mnist_model.pkl")

st.set_page_config(page_title="MNIST Digit Recognizer", layout="centered")
st.title("✍️ MNIST Digit Recognition (KNN)")
st.markdown("Draw a digit (0–9) below and click **Predict**:")

# Drawing Canvas
canvas_result = st_canvas(
    fill_color="rgba(0, 0, 0, 0)",  # Transparent fill
    stroke_width=10,
    stroke_color="#FFFFFF",        # White stroke
    background_color="#000000",    # Black background
    width=192,
    height=192,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button("🧠 Predict Digit"):
    if canvas_result.image_data is not None:
        # Show raw canvas image
        st.image(canvas_result.image_data, caption="🖌 Raw Canvas Image", width=150)

        # Convert to grayscale (take first channel)
        img = canvas_result.image_data[:, :, 0].astype(np.uint8)

        # Invert colors (MNIST is white background, black digit)
        img = 255 - img

        # Resize directly to 28x28 (no cropping)
        img_resized = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)

        # Normalize pixel values to 0–16 (like MNIST training data)
        img_scaled = (img_resized / 255.0) * 16

        # Flatten to match model input
        img_flatten = img_scaled.flatten().reshape(1, -1)

        # Predict
        prediction = model.predict(img_flatten)[0]

        # Show prediction
        st.success(f"🎯 Predicted Digit: **{prediction}**")

        # Show final image sent to model
        st.image(img_scaled, width=150, clamp=True, caption="🖼 Image Sent to Model")
    else:
        st.warning("Please draw something before predicting.")
