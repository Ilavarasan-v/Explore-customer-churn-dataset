# Day 3 Task Train and Evaluate a Churn Prediction Model

## What this is

Use the **cleaned, feature engineered dataset you created during Day 2**. This should include your preprocessing, feature engineering, and target column (`has_churned`, where `0 = stayed` and `1 = churned`).

Your Day 3 work should build directly on your own Day 2 output rather than using a provided reference dataset.

---

## What to do

### 1. Set up a proper evaluation split

Split your dataset into training and testing sets (e.g. 80/20).

Think carefully about whether a simple random split is appropriate or whether you should **stratify on the target**. Churn datasets are often imbalanced, so your split should preserve the class distribution where appropriate.

---

### 2. Train two different models

Choose **two meaningfully different machine learning models** to predict `has_churned`.

Examples include:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost (optional)

Perform appropriate preprocessing:

- Encode categorical variables.
- Scale numerical features if required by the model.
- Fit preprocessing **only on the training data** to avoid data leakage.

---

### 3. Evaluate and compare

Evaluate both models on the held out test set and report:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Then answer the following questions:

- Which evaluation metric matters most for a churn prediction problem, and why?
- What is the business cost of false positives versus false negatives?
- Which model would you recommend deploying, and why?

---

### 4. Examine your features critically

Before finalizing your model:

- Check correlations between features and the target.
- Check correlations among features to identify multicollinearity.
- Think about whether every feature would actually be available **at the time a prediction needs to be made** in a real business scenario.
- If you discover any feature that could introduce target leakage or unrealistic information, explain your reasoning and remove it if necessary.

---

### 5. Check for overfitting

Compare training and testing performance for both models.

If training performance is significantly better than testing performance:

- Explain why you believe overfitting occurred.
- Describe how you would address it (for example: regularization, pruning, fewer features, simpler models, cross-validation, or collecting more data).

---

### 6. Write a short report (`MODEL_REPORT.md`)

Your report should include:

- Train/test split strategy
- Preprocessing pipeline
- Models used
- Evaluation metrics (side by side comparison)
- Which metric you prioritized and why
- Final model recommendation
- Feature analysis and any removed features
- Evidence of overfitting (if any) and how you handled it
- What you would improve with more time

---

### 7. Deliverables

Submit:

- Your training and evaluation code (Notebook or Python script)
- `MODEL_REPORT.md`
- Your cleaned Day 2 dataset
- Git commits showing your progress

---

## What we're looking for

- Correct, leak free train/test methodology
- Appropriate preprocessing performed only on training data
- Thoughtful model comparison
- Business focused metric selection
- Critical examination of features for leakage and usefulness
- Clear explanations for every modeling decision

---

## If you have time left

- Try a third model.
- Perform hyperparameter tuning.
- Use cross validation.
- Examine feature importances or model coefficients.
- Compare your findings with the insights from your Day 2 exploratory analysis.

---

## This afternoon

Be prepared to present:

- Both models and their results
- Why you selected your evaluation metric
- Why you recommend your chosen model
- Any feature engineering or feature removal decisions
- Any overfitting you observed
- What you would improve with more time

You should also expect a live request to modify part of your modeling pipeline and explain the impact of the change.
