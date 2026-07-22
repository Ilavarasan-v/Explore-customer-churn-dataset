# Customer Churn Data Preprocessing

## Overview

This project focuses on cleaning and preparing a real-world telecom customer churn dataset for machine learning. The raw dataset contains missing values, inconsistent formatting, incorrect data types, duplicate records, outliers, and mixed date formats.

The goal of this project is to transform the raw dataset into a clean, consistent, and machine-learning-ready dataset that can be used to build a customer churn prediction model.

---

## Dataset Information

- **Dataset:** Telecom Customer Churn
- **Total Records:** 431
- **Target Column:** `has_churned`

---

## Project Workflow

### 1. Data Exploration (EDA)

- Explored dataset structure
- Identified missing values
- Checked data types
- Examined value distributions
- Detected duplicate records
- Identified outliers
- Reviewed categorical inconsistencies

---

### 2. Data Cleaning

Performed the following preprocessing steps:

- Removed unnecessary index column
- Standardized categorical values
- Converted numeric columns stored as text
- Parsed multiple date formats into datetime
- Handled missing values
- Corrected unrealistic values
- Removed duplicate records

---

### 3. Feature Engineering

Created additional features to improve model performance:

- **avg_charge_per_month**
- **tenure_group**
- **high_support**
- **is_senior**

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Project Structure

```
Explore-customer-churn-dataset/
│
├── notebook/
│   └── customer_churn_preprocessing.ipynb
│
├── output/
│   └── clean_customer_churn.csv
│
├── EDA_REPORT.md
├── README.md
└── requirements.txt
```

---

## Output

The project generates:

- ✅ Cleaned customer churn dataset
- ✅ Feature-engineered dataset
- ✅ EDA report
- ✅ Jupyter notebook containing the complete preprocessing workflow

---

## Key Learnings

Through this project I learned how to:

- Perform exploratory data analysis on messy datasets
- Handle missing values using appropriate strategies
- Standardize inconsistent categorical data
- Convert incorrect data types
- Detect and treat outliers
- Engineer meaningful features for predictive modeling
- Prepare data for machine learning workflows

---

## Future Work

The cleaned dataset will be used to build and evaluate a Customer Churn Prediction model using machine learning algorithms.

---
