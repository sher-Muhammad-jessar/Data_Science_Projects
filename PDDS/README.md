# 🌾 Pest and Disease Detection System (PDDS)

An AI-powered mobile-only application that helps farmers detect crop diseases and pest infections by scanning plants using their smartphone camera. The app uses a trained deep learning model to identify diseases and recommend treatment solutions.

---

## 📱 Features

- 📷 **Scan Crops**: Take or upload photos of crops to detect diseases.
- 🧠 **AI-Powered Detection**: Uses Convolutional Neural Networks (CNN) trained on real crop disease data.
- 📊 **Health Dashboard**: Tracks the progress of infected crops over time.
- 💊 **Smart Suggestions**: Recommends remedies or products based on disease type.
- 🌐 **Offline Capability (optional)**: Basic disease detection can work without internet once the model is downloaded.

---

## 🧠 Technologies Used

- Python 🐍
- TensorFlow / Keras 🧠
- NumPy & OpenCV 📊
- Streamlit 🌐 (for the demo interface)
- Matplotlib & Seaborn 📉
- Dataset Source: Kaggle (PlantVillage or similar)

---

## 📁 Project Structure
PDDS/
│
├── app.py # Streamlit app for image upload and prediction
├── model/
│ └── final_model.h5 # Trained CNN model
├── dataset/
│ └── (Kaggle crop disease images)
├── utils/
│ └── preprocessing.py # Image preprocessing and utilities
├── README.md # Project documentation
└── requirements.txt # Required Python packages

