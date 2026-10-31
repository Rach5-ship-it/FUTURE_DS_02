import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "dataset", "cleaned_telco_churn.csv")
OUT = os.path.join(BASE, "visualization")
os.makedirs(OUT, exist_ok=True)

# Load cleaned data
df = pd.read_csv(DATA)

# Ensure numeric columns are numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna(subset=["TotalCharges"]).copy()

# Overall churn
churn_counts = df["Churn"].value_counts()
churn_rate = (df["Churn"].eq("Yes").mean() * 100)

# Tenure groups
bins = [0, 6, 12, 24, 48, 72]
labels = ["0-6 months", "7-12 months", "13-24 months", "25-48 months", "49-72 months"]
df["TenureGroup"] = pd.cut(df["tenure"], bins=bins, labels=labels, include_lowest=True)

# Helper for bar charts
def save_bar(series, title, xlabel, ylabel, filename, rotation=0):
    ax = series.plot(kind="bar", figsize=(9, 5))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=rotation, ha="right" if rotation else "center")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT, filename), dpi=150)
    plt.close()

# 1. Overall churn rate
plt.figure(figsize=(7, 5))
plt.bar(["Stayed", "Churned"], [churn_counts.get("No", 0), churn_counts.get("Yes", 0)])
plt.title("Customer Churn Overview")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(os.path.join(OUT, "churn_overview.png"), dpi=150)
plt.close()

# 2. Churn rate by contract
contract_rate = df.groupby("Contract")["Churn"].apply(lambda x: (x == "Yes").mean() * 100).sort_values(ascending=False)
save_bar(contract_rate, "Churn Rate by Contract Type", "Contract", "Churn Rate (%)", "churn_by_contract.png", 15)

# 3. Churn rate by tenure
tenure_rate = df.groupby("TenureGroup", observed=True)["Churn"].apply(lambda x: (x == "Yes").mean() * 100)
save_bar(tenure_rate, "Churn Rate by Customer Tenure", "Tenure", "Churn Rate (%)", "churn_by_tenure.png")

# 4. Churn rate by payment method
payment_rate = df.groupby("PaymentMethod")["Churn"].apply(lambda x: (x == "Yes").mean() * 100).sort_values(ascending=False)
save_bar(payment_rate, "Churn Rate by Payment Method", "Payment Method", "Churn Rate (%)", "churn_by_payment.png", 20)

# 5. Churn rate by internet service
internet_rate = df.groupby("InternetService")["Churn"].apply(lambda x: (x == "Yes").mean() * 100).sort_values(ascending=False)
save_bar(internet_rate, "Churn Rate by Internet Service", "Internet Service", "Churn Rate (%)", "churn_by_internet.png")

# 6. Churn rate by tech support
support_rate = df.groupby("TechSupport")["Churn"].apply(lambda x: (x == "Yes").mean() * 100).sort_values(ascending=False)
save_bar(support_rate, "Churn Rate by Tech Support", "Tech Support", "Churn Rate (%)", "churn_by_support.png", 15)

# Save summary metrics
summary = pd.DataFrame({
    "Metric": [
        "Customers analyzed", "Overall churn rate", "Average tenure - stayed",
        "Average tenure - churned", "Average monthly charge - stayed",
        "Average monthly charge - churned", "Average total charges - stayed",
        "Average total charges - churned"
    ],
    "Value": [
        len(df), round(churn_rate, 2),
        round(df.loc[df.Churn == "No", "tenure"].mean(), 2),
        round(df.loc[df.Churn == "Yes", "tenure"].mean(), 2),
        round(df.loc[df.Churn == "No", "MonthlyCharges"].mean(), 2),
        round(df.loc[df.Churn == "Yes", "MonthlyCharges"].mean(), 2),
        round(df.loc[df.Churn == "No", "TotalCharges"].mean(), 2),
        round(df.loc[df.Churn == "Yes", "TotalCharges"].mean(), 2),
    ]
})
summary.to_csv(os.path.join(OUT, "summary_metrics.csv"), index=False)

print(f"Customers analyzed: {len(df)}")
print(f"Overall churn rate: {churn_rate:.2f}%")
print("\nChurn rate by contract:")
print(contract_rate.round(2))
print("\nChurn rate by tenure:")
print(tenure_rate.round(2))
print("\nChurn rate by payment method:")
print(payment_rate.round(2))
print("\nChurn rate by internet service:")
print(internet_rate.round(2))
print("\nChurn rate by tech support:")
print(support_rate.round(2))
print("\nAnalysis complete. Visualizations saved in visualization/.")
