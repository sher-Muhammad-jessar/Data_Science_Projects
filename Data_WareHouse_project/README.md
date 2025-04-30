# 🏥 Healthcare ETL and Disease Prediction System

This project is a complete ETL (Extract, Transform, Load) pipeline integrated with a prediction module to forecast disease case counts using historical data. It extracts data from multiple healthcare sources (patients, billing, pharmacy), cleans and transforms it, loads it into a Data Warehouse, and performs linear regression to predict disease trends.

---

## 📌 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Data Flow](#data-flow)
- [ETL Process](#etl-process)
- [Prediction Module](#prediction-module)
- [Sample Output](#sample-output)
- [Contributing](#contributing)


---

## 🚀 Features

- Extracts data from:
  - Patient Management System
  - Hospital Billing System
  - Pharmacy Inventory
  - External Public Health CSV
- Cleans and transforms raw data (dates, nulls, types)
- Loads data into a **MySQL Data Warehouse**
- Populates fact and dimension tables (Star Schema)
- Predicts future case counts for any disease (e.g., Flu, Dengue)
- Uses **Linear Regression** for simple time series forecasting

---

## 🛠️ Technologies Used

- **Python** (Pandas, MySQL Connector, Scikit-learn)
- **MySQL** (Data Warehouse Schema)
- **Pandas** (Data Transformation & Manipulation)
- **Scikit-learn** (Linear Regression Model)
- **Jupyter Notebook** / Script (.py)

---

## 🔁 Data Flow

\`\`\`text
[Raw Data Sources]
       ↓
[Python ETL Script]
       ↓
[Transformed Data]
       ↓
[MySQL Data Warehouse (Star Schema)]
       ↓
[Prediction Module (Linear Regression)]
       ↓
[Predicted Disease Case Counts]
\`\`\`

---

## 🧪 ETL Process

The \`extract_from_sources()\`, \`transform_data()\`, and \`load_to_warehouse()\` functions perform:

- **Extract**: Read data from MySQL and CSV
- **Transform**: Clean, convert dates, fill missing values, cast types
- **Load**: Insert data into Data Warehouse (Star Schema)

---

## 📈 Prediction Module

The function \`predict_case_counts(disease_name='Flu')\`:

- Pulls monthly case counts of a disease from the Data Warehouse
- Fits a **Linear Regression** model
- Predicts case counts for future months
- Plots or prints the predictions (can be extended for dashboards)

---

## 🧾 Sample Output
-✅ Connected to database successfully!
-📊 Predicting future disease cases using Linear Regression...

-Enter Disease Name: Dengue

-Predicted case counts for the next 6 months:
-2025-05: 135 cases
-2025-06: 145 cases
-2025-07: 154 cases
-2025-08: 162 cases
-2025-09: 170 cases
-2025-10: 178 cases

-📉 Plot generated successfully!




## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork the repo
2. Create a branch (\`git checkout -b feature-x\`)
3. Commit your changes
4. Push and open a Pull Request



> Built with ❤️ by Sher Muhammad — helping hospitals make data-driven decisions.
