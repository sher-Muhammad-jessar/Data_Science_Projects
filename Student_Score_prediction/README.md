# 📊 Student Performance Predictor

This project uses **Linear Regression** to predict a student's performance (score) based on key factors such as:

- 📚 Study Hours  
- 🏫 Attendance  
- 💤 Sleep Hours  

The model is trained using scikit-learn and visualized with matplotlib to provide insights on how each factor affects academic performance.

---

## 🔍 Features

- Predict scores using multiple features (study hours, attendance, sleep)  
- Automatically caps unrealistic values (e.g., >20 hours of study)  
- Visualizes prediction trends using scatter and line plots  
- Clean and modular Python code  

---

## 🛠 Technologies Used

- Python 🐍  
- pandas  
- numpy  
- matplotlib  
- scikit-learn  

---

## 📁 Dataset

The dataset includes the following columns:

- `StudyHours` – number of hours a student studies  
- `Attendance` – class attendance percentage  
- `SleepHours` – average sleep hours  
- `Score` – actual performance score (label)  

> You can replace or expand the dataset (`df`) as needed.

---


## 📈 Example Output

<pre><code>
Capping Study Hours to max 20.
Study Hours (Capped): 5.0 → Predicted Score: 52.34
Study Hours (Capped): 18.0 → Predicted Score: 86.45
Study Hours (Capped): 20.0 → Predicted Score: 88.77
</code></pre>


## 🚀 How to Run

```bash
# Step 1: Clone the repo
git clone https://github.com/yourusername/student-performance-predictor.git
cd student-performance-predictor

# Step 2: Install required packages
pip install numpy pandas matplotlib scikit-learn

# Step 3: Run the script
python predictor.py

---
