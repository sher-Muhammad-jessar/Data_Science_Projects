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
## ⚙️ How It Works

1. **Preprocess input image** (resize, normalize).
2. **Feed image into CNN model**.
3. **Predict disease class**.
4. **Show class label and prediction confidence**.
5. **Recommend treatment based on class**.

---
## 📌 Future Enhancements

- 📱 **Convert the system into a fully functional mobile app** using Flutter or React Native.

- 🛰️ **Add GPS-based crop monitoring** to provide localized disease insights and trends.

- 🌐 **Enable offline-first capability** to ensure the model works without active internet, especially in remote farming areas.

- 🛒 **Integrate with nearby pesticide suppliers** to recommend and connect farmers directly with available treatments.

