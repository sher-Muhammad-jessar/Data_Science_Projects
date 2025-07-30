import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model('final_model.h5')
class_names = ['Pepper__bell___Bacterial_spot',
               'Pepper__bell___healthy',
               'PlantVillage',
               'Potato___Early_blight',
               'Potato___healthy',
               'Potato___Late_blight',
               'Tomato__Target_Spot',
               'Tomato__Tomato_mosaic_virus',
               'Tomato__Tomato_YellowLeaf__Curl_Virus',
               'Tomato_Bacterial_spot',
               'Tomato_Early_blight',
               'Tomato_healthy',
               'Tomato_Late_blight',
               'Tomato_Leaf_Mold',
               'Tomato_Septoria_leaf_spot',
               'Tomato_Spider_mites_Two_spotted_spider_mite'
               
               ]

# Prediction function
def predict_disease(IMG):
    IMG = IMG.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(IMG)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    st.write("Prediction raw output:", prediction)
    st.write("Prediction shape:", prediction.shape)

    predicted_index = np.argmax(prediction)

    if predicted_index >= len(class_names):
        raise ValueError(f"Predicted index {predicted_index} is out of range for class_names with length {len(class_names)}")

    predicted_class = class_names[predicted_index]
    confidence = round(100 * np.max(prediction), 2)
    return predicted_class, confidence


# Streamlit UI
st.set_page_config(page_title="Pest and Disease Detection System", layout='centered')
st.title("🌾 Crop Disease Detection App")
st.write("Upload a leaf image of your infected crop")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_data = Image.open(uploaded_file)
    st.image(image_data, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        with st.spinner("Analyzing..."):
            label, confidence = predict_disease(image_data)
            st.success(f"Prediction: **{label}** with **{confidence}%** confidence.")
