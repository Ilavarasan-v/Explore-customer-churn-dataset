# Day 2 Task — Clean & Prepare the Customer Churn Dataset

## What this is

`messy_customer_churn.csv` is a telecom customer dataset with **431 rows** and
a `has_churned` target column this is real world messy, not textbook-clean.
It has missing values, inconsistent formatting, duplicates, and outliers, all
mixed in with a genuine underlying signal.

**This dataset feeds directly into Day 3**, where you'll train a model to
predict churn using what you clean and engineer today. Decisions you make
today (how you handle missing values, outliers, encoding) will affect what
you're able to do tomorrow so make choices you can defend, not just ones
that make the errors go away.

## What to do

### 1. Explore first (don't touch anything yet)
Load the data and actually look at it before cleaning:
- What are the dtypes? Do they match what the values actually represent?
- What does each column's value distribution look like?
- Where is data missing and does it look random or systematic?
- Are there duplicate rows or duplicate customers?
- Are there values that are technically valid but practically impossible
  (e.g. an age of 199)?

### 2. Clean the data
For each issue you find, fix it and know *why* you fixed it that way:
- Standardize inconsistent categorical values (e.g. the same category spelled
  multiple ways)
- Convert columns to the correct dtype (numbers stored as text, currency
  symbols, etc.)
- Decide how to handle missing values per column drop, impute, or flag
  and be ready to justify the choice per column, not as one blanket rule
- Decide how to handle outliers are they data-entry errors to fix/remove,
  or real extreme values to keep?
- Handle duplicate rows/customers
- Parse inconsistent date formats into one consistent format

### 3. Engineer features
Add at least 3 engineered features that could plausibly help predict churn
tomorrow. Some ideas (you don't have to use these better if you think of
your own):
- Something derived from tenure or signup date
- A ratio or derived value from the charge columns
- A binned/bucketed version of a continuous variable
- Something derived from support ticket volume

### 4. Write a short EDA report (`EDA_REPORT.md`)
In your own words, cover:
- What was wrong with the raw data (be specific which columns, what kind
  of issue, roughly how many rows affected)
- The choices you made cleaning each issue, and why
- What you found exploring the data anything that looks related to churn?
- The features you engineered and your reasoning for each

### 5. Deliverables
- `clean_customer_churn.csv` your cleaned, feature engineered dataset
- Your cleaning/feature engineering code (script or notebook)
- `EDA_REPORT.md`
- Incremental git commits, not one dump at the end

## What we're looking for

- Whether you actually inspect data before changing it, rather than writing
  cleaning code on autopilot
- Whether your handling of missing values and outliers is reasoned per column,
  not a single copy pasted approach applied everywhere
- Whether your engineered features make domain sense for predicting churn
- Whether you can explain every choice when asked

