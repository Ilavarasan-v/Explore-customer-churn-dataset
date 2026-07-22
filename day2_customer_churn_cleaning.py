#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('messy_customer_churn.csv')
print(df.shape)
df.dtypes

# In[3]:


df

# In[4]:


print("Shape:", df.shape)

df.head()

# In[5]:


df.info()

# In[6]:


df.describe(include="all").T

# In[7]:


missing = pd.DataFrame({
    "Missing Values": df.isnull().sum(),
    "Percentage": (df.isnull().mean()*100).round(2)
})

missing.sort_values("Missing Values", ascending=False)

# In[8]:


print("Duplicate rows:", df.duplicated().sum())

# In[9]:


df["customer_id"].duplicated().sum()

# In[10]:


for col in df.select_dtypes(include="object"):
    print("="*50)
    print(col)
    print(df[col].value_counts(dropna=False))

# In[11]:


df.describe()

# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns

numeric_cols = df.select_dtypes(include="number").columns

for col in numeric_cols:
    plt.figure(figsize=(6,2))
    sns.boxplot(x=df[col])
    plt.title(col)
    plt.show()

# In[13]:


df.hist(figsize=(12,8))
plt.tight_layout()

# In[15]:


categorical_cols = df.select_dtypes(include="object").columns

for col in categorical_cols:
    print("=" * 60)
    print(f"Column: {col}")
    print(f"Unique Values: {df[col].nunique(dropna=False)}")
    print(df[col].value_counts(dropna=False))
    print()

# In[16]:


print(df.dtypes)

# In[17]:


df["monthly_charges"].head(20)

# In[18]:


df["total_charges"].head(20)

# In[19]:


df["signup_date"].head(20)

# In[20]:


duplicate_customers = df[df["customer_id"].duplicated(keep=False)]
duplicate_customers.sort_values("customer_id")

# In[21]:


df.drop(columns=["Unnamed: 0"], inplace=True)

# In[23]:


df.columns

# In[24]:


object_cols = df.select_dtypes(include="object").columns

for col in object_cols:
    df[col] = df[col].astype(str).str.strip()

# In[25]:


for col in object_cols:
    print(col)
    print(df[col].head())

# In[26]:


categorical_cols = [
    "gender",
    "contract_type",
    "payment_method",
    "has_churned"
]

for col in categorical_cols:
    df[col] = df[col].str.lower()

# In[27]:


for col in categorical_cols:
    print("="*40)
    print(col)
    print(df[col].value_counts(dropna=False))

# In[28]:


df["monthly_charges"].sample(15)

# In[29]:


df["total_charges"].sample(15)

# In[ ]:


df["monthly_charges"].sample(15)

# In[31]:


df["total_charges"].sample(15)

# In[32]:


df["monthly_charges"] = (
    df["monthly_charges"]
      .str.replace("$", "", regex=False)
)

df["monthly_charges"] = pd.to_numeric(
    df["monthly_charges"],
    errors="coerce"
)

# In[33]:


df["monthly_charges"].dtype

# In[34]:


df["total_charges"] = (
    df["total_charges"]
      .str.replace("$", "", regex=False)
      .str.replace(",", "", regex=False)
)

df["total_charges"] = pd.to_numeric(
    df["total_charges"],
    errors="coerce"
)

# In[35]:


df["total_charges"].dtype

# In[36]:


df.isnull().sum()

# In[37]:


df["signup_date"].sample(20)

# In[38]:


df["signup_date"] = pd.to_datetime(
    df["signup_date"],
    format="mixed",
    errors="coerce"
)

# In[39]:


df["signup_date"] = pd.to_datetime(
    df["signup_date"],
    errors="coerce"
)

# In[42]:


df["signup_date"].head()


# In[43]:


df["signup_date"].dtype

# In[44]:


df.info()

# In[45]:


df.isnull().sum()

# In[46]:


df["age"] = df["age"].fillna(df["age"].median())

# In[47]:


df["tenure_months"] = df["tenure_months"].fillna(df["tenure_months"].median())

# In[48]:


df["num_support_tickets"] = df["num_support_tickets"].fillna(
    df["num_support_tickets"].median()
)

# In[49]:


df["gender"] = df["gender"].fillna(df["gender"].mode()[0])

# In[51]:


df["contract_type"] = df["contract_type"].fillna(
    df["contract_type"].mode()[0]
)

# In[52]:


df["payment_method"] = df["payment_method"].fillna(
    df["payment_method"].mode()[0]
)

# In[53]:


df["monthly_charges"] = df["monthly_charges"].fillna(
    df["monthly_charges"].median()
)

# In[54]:


df["total_charges"] = df["total_charges"].fillna(
    df["total_charges"].median()
)

# In[55]:


median_date = df["signup_date"].dropna().sort_values().iloc[len(df["signup_date"].dropna())//2]

df["signup_date"] = df["signup_date"].fillna(median_date)

# In[56]:


mask = df["customer_id"].isna()

df.loc[mask, "customer_id"] = [
    f"UNKNOWN_{i}" for i in range(mask.sum())
]

# In[57]:


df = df.dropna(subset=["has_churned"])

# In[58]:


df.isnull().sum()

# In[60]:


import numpy as np

# In[61]:


df.loc[(df["age"] < 18) | (df["age"] > 100), "age"] = np.nan

df["age"] = df["age"].fillna(df["age"].median())

# In[63]:


df.loc[
    (df["tenure_months"] < 0) |
    (df["tenure_months"] > 120),
    "tenure_months"
] = np.nan

df["tenure_months"] = df["tenure_months"].fillna(
    df["tenure_months"].median()
)

# In[64]:


df.describe()

# In[65]:


print("Duplicate rows:", df.duplicated().sum())

# In[66]:


df = df.drop_duplicates()

# In[67]:


df["customer_id"].duplicated().sum()

# In[68]:


duplicates = df[df["customer_id"].duplicated(keep=False)]
duplicates.sort_values("customer_id")

# In[69]:


df = df.drop_duplicates(subset="customer_id", keep="first")

# In[71]:


# this is Feature Engineering part
# Feature 1 – Average Charge Per Month
df["avg_charge_per_month"] = (
    df["total_charges"] / df["tenure_months"].replace(0, 1)
)

# In[72]:


# Feature 2 – Tenure Group
df["tenure_group"] = pd.cut(
    df["tenure_months"],
    bins=[0,12,24,48,120],
    labels=["New","1-2 Years","2-4 Years","4+ Years"]
)

# In[73]:


# Feature 3 – High Support Ticket Flag
df["high_support"] = (
    df["num_support_tickets"] >= 3
).astype(int)

# In[74]:


# Feature 4 – Senior Citizen
df["is_senior"] = (
    df["age"] >= 60
).astype(int)

# In[77]:


df.to_csv("clean_customer_churn.csv", index=False)


# In[78]:


import os

os.makedirs("output", exist_ok=True)
df.to_csv("output/clean_customer_churn.csv", index=False)


# In[79]:


import os

print(os.getcwd())

# In[ ]:



