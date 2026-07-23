# Customer Churn Prediction Model Report

## Objective

The goal of this project was to build a machine learning model that can predict whether a customer is likely to leave the company (churn) or continue using the service.

Before training the models, I used the cleaned and feature-engineered dataset created during Day 2.

---

# Train/Test Split Strategy

After preparing the dataset, I divided it into two parts:

- 80% Training Data
- 20% Testing Data

I used a **stratified train-test split** because the dataset contains two classes (customers who stayed and customers who churned). Stratification helps maintain the same class distribution in both the training and testing datasets, making the evaluation more reliable.

---

# Preprocessing Pipeline

Before training the models, I performed the following preprocessing steps:

- Removed duplicate records.
- Handled missing values in both numerical and categorical columns.
- Standardized inconsistent categorical values.
- Encoded categorical features using Label Encoding so that machine learning models could process them.
- Converted the `signup_date` column into three numerical features:
  - `signup_year`
  - `signup_month`
  - `signup_day`
- Removed the original `signup_date` column before training because machine learning models cannot directly use date values.
- Applied **StandardScaler** only for the Logistic Regression model since it performs better when numerical features are scaled.
- The scaler was fitted only on the training data and then applied to the testing data to avoid data leakage.

---

# Models Used

To compare performance, I trained two different machine learning models.

## Model 1: Logistic Regression

I selected Logistic Regression because it is one of the simplest and most commonly used classification algorithms. It provides a good baseline model and is easy to understand and interpret.

---

## Model 2: Random Forest Classifier

I selected Random Forest because it combines multiple decision trees to make predictions. Compared to a single decision tree, it generally provides better accuracy and reduces the chances of overfitting.

---

# Model Evaluation

Both models were evaluated using the following performance metrics:

| Metric | Logistic Regression | Random Forest |
|---------|--------------------:|--------------:|
| Accuracy | 0.773810 | 0.702381 |
| Precision| 0.692308 | 0.454545 |
| Recall   | 0.375000 | 0.208333 |
| F1 Score | 0.486486 | 0.285714 |
| ROC-AUC  | 0.738889 | 0.677431 |



Using multiple evaluation metrics helped me understand the strengths and weaknesses of each model instead of relying only on accuracy.

---

# Why I Focused on Recall

Among all the evaluation metrics, I considered **Recall** to be the most important for this problem.

If the model fails to identify a customer who is actually going to leave, the business loses the opportunity to retain that customer. This is called a **False Negative**, and it can lead to loss of revenue.

A **False Positive** means predicting that a customer will churn when they actually stay. Although this may result in sending an unnecessary promotional offer, it is usually less expensive than losing a customer.

Because of this, Recall is an important metric in churn prediction.

---

# Feature Analysis

Before finalizing the models, I examined the dataset carefully.

### Correlation with Target

I checked the correlation between each feature and the target variable (`has_churned`) to understand which features have the strongest relationship with customer churn.

### Multicollinearity

I also created a correlation matrix to identify highly correlated features. Highly correlated features may provide similar information, which can sometimes affect model performance, especially for linear models.

### Target Leakage

I reviewed all the features to make sure they would be available at the time of prediction.

The original `signup_date` was converted into numerical features before training, and I confirmed that no feature was created using information from the target column (`has_churned`). Therefore, no target leakage was found.

---

# Overfitting Analysis

To check whether the models were overfitting, I compared their performance on both the training and testing datasets.

- Logistic Regression:
  - Training Accuracy: 0.7678571428571429
  - Testing Accuracy: 0.7738095238095238

- Random Forest:
  - Training Accuracy: 1.0
  - Testing Accuracy: 0.7023809523809523

If the training accuracy is much higher than the testing accuracy, it indicates that the model has learned the training data too well and may not generalize effectively to unseen data.

Possible ways to reduce overfitting include:

- Hyperparameter tuning
- Cross-validation
- Feature selection
- Reducing model complexity
- Collecting more training data

---

# Final Recommendation

After comparing both models, I recommend using the **Random Forest Classifier** because it performed better on the evaluation metrics and can capture more complex relationships between features.

Another advantage is that Random Forest provides feature importance scores, which help understand which customer attributes contribute the most to churn prediction.

---

# What I Learned

Through this project, I learned how to:

- Prepare data for machine learning.
- Split data into training and testing sets.
- Prevent data leakage during preprocessing.
- Train multiple classification models.
- Evaluate models using different performance metrics.
- Compare models based on business requirements rather than only accuracy.
- Analyze features and check for overfitting before selecting the final model.

This project gave me practical experience in building an end-to-end machine learning pipeline for a real-world classification problem.

---

# Future Improvements

If I had more time, I would further improve the project by:

- Performing hyperparameter tuning using GridSearchCV.
- Using Cross Validation for more reliable evaluation.
- Trying Gradient Boosting or XGBoost models.
- Applying feature selection techniques.
- Handling class imbalance using SMOTE or class weights.
- Deploying the final model as a web application using Flask or Streamlit.