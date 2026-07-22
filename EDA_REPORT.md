# EDA Report – Customer Churn Dataset

## Project Overview

For this task, my objective was to clean and prepare a messy telecom customer churn dataset so that it could be used for machine learning in the next stage. Before making any changes, I explored the dataset to understand its structure, identify data quality issues, and decide on the most appropriate cleaning strategy.

The dataset contained 431 customer records with **has_churned** as the target variable.

---

# What I Found During Exploration

After exploring the dataset, I noticed several common real-world data quality problems.

### Missing Values

Several columns contained missing values. Instead of applying one rule to every column, I handled each column based on the type of data it contained.

- Numerical columns such as **age**, **tenure_months**, **monthly_charges**, **total_charges**, and **num_support_tickets** were filled using the median because it is less affected by extreme values.
- Categorical columns such as **gender**, **contract_type**, and **payment_method** were filled using the most frequent value.
- Missing **signup_date** values were replaced using the median date from the dataset.
- A few missing **customer_id** values were replaced with placeholder IDs to maintain unique records.
- Rows with missing **has_churned** values were removed because this is the target column and cannot be guessed.

---

### Incorrect Data Types

While exploring the dataset, I noticed that some numeric columns were stored as text.

For example:

- monthly_charges contained values such as **$75.29**
- total_charges contained values such as **$4,325.08**
- signup_date was stored as plain text using multiple date formats.

Before converting these columns, I removed currency symbols and commas, then converted them to their appropriate numeric and datetime data types.

---

### Inconsistent Formatting

Some categorical columns contained inconsistent formatting.

Examples included:

- Male, male, MALE
- Yes, yes, YES

These values all represent the same category, so I removed extra spaces and converted all categorical values to lowercase to maintain consistency.

---

### Outliers

During exploration, I identified values that were technically present but practically impossible.

Some examples were:

- Age = 0
- Age = 199
- Tenure = -3 months
- Tenure = 999 months

These appeared to be data entry errors rather than genuine customer records.

Instead of simply deleting those rows, I treated them as missing values and replaced them using the median of the column.

---

### Duplicate Records

I checked both duplicate rows and duplicate customer IDs.

Any exact duplicate records were removed while ensuring that only one record existed for each customer.

---

# Feature Engineering

After cleaning the dataset, I created several additional features that could help improve the churn prediction model.

### 1. Average Charge Per Month

I created a feature called **avg_charge_per_month**, which calculates the average monthly spending for each customer.

This gives a better understanding of customer spending behaviour than total charges alone.

---

### 2. Tenure Group

I grouped customers based on how long they had been with the company.

The groups were:

- New
- 1–2 Years
- 2–4 Years
- 4+ Years

This feature helps identify whether newer customers are more likely to churn than long-term customers.

---

### 3. High Support Flag

I created a binary feature called **high_support**.

Customers with three or more support tickets were marked as 1, while the remaining customers were marked as 0.

Frequent support requests may indicate customer dissatisfaction, which could contribute to churn.

---

### 4. Senior Customer

I also created an **is_senior** feature.

Customers aged 60 years or above were assigned a value of 1, and all others were assigned 0.

This allows the model to determine whether age influences customer churn.

---

# Key Observations

While exploring the data, I observed several interesting patterns.

- The dataset contained both numerical and categorical missing values.
- Currency symbols prevented direct numeric conversion.
- Multiple date formats required standardization.
- Several values were obvious data entry errors.
- Customers with longer tenure generally accumulated higher total charges.
- Customers with more support tickets appeared more likely to churn, making this a potentially useful feature for prediction.

---

# Final Outcome

After completing the preprocessing steps, the dataset became clean, consistent, and suitable for machine learning.

The final deliverables include:

- **clean_customer_churn.csv**
- **Customer Churn Cleaning Notebook**
- **EDA_REPORT.md**

This cleaned dataset is now ready for building and evaluating a customer churn prediction model in the next stage of the project.