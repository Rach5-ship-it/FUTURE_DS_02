import pandas as pd

INPUT = "dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
OUTPUT = "dataset/cleaned_telco_churn.csv"

df = pd.read_csv(INPUT)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print("Missing values after conversion:")
print(df.isnull().sum())

# Remove rows where TotalCharges could not be converted
before = len(df)
df = df.dropna(subset=["TotalCharges"]).copy()
print(f"\nRows removed: {before - len(df)}")
print(f"Rows after cleaning: {len(df)}")

df.to_csv(OUTPUT, index=False)
print(f"Cleaned dataset saved to {OUTPUT}")
