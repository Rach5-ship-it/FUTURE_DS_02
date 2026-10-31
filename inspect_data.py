import pandas as pd

# Load the dataset
df = pd.read_csv("dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Basic information
print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())