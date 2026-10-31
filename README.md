# FUTURE_DS_02 – Customer Retention & Churn Analysis

## Project Overview

This project analyzes customer data for a subscription-based business to identify churn patterns, retention drivers and customer lifetime trends.

## Objective

- Measure overall customer churn
- Identify high-risk customer segments
- Analyze churn by contract, tenure, payment method and internet service
- Examine the relationship between tech support and churn
- Generate actionable business recommendations

## Tools Used

- Python
- Pandas
- Matplotlib
- CSV dataset

## Project Structure

```text
FUTURE_DS_02/
├── analysis/
│   └── churn_analysis.py
├── dataset/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── cleaned_telco_churn.csv
├── report/
│   └── task2_report.md
├── visualization/
│   ├── churn_overview.png
│   ├── churn_by_contract.png
│   ├── churn_by_tenure.png
│   ├── churn_by_payment.png
│   ├── churn_by_internet.png
│   ├── churn_by_support.png
│   └── summary_metrics.csv
├── clean_data.py
├── inspect_data.py
└── README.md
```

## Key Results

- Customers analyzed: **7,032**
- Overall churn rate: **26.58%**
- Highest contract churn: **Month-to-month – 42.71%**
- Lowest contract churn: **Two year – 2.85%**
- Highest tenure-group churn: **0–6 months – 53.33%**
- Highest payment-method churn: **Electronic check – 45.29%**
- Highest internet-service churn: **Fiber optic – 41.89%**
- Churn with no tech support: **41.65%**
- Churn with tech support: **15.20%**

## How to Run

From the `FUTURE_DS_02` folder:

```bash
python clean_data.py
python inspect_data.py
python analysis/churn_analysis.py
```

The analysis script generates the visualizations inside the `visualization` folder.

## Main Business Recommendations

1. Strengthen onboarding during the first six months.
2. Encourage suitable month-to-month customers to move to longer contracts.
3. Promote convenient automatic payment methods.
4. Increase awareness and adoption of technical support.
5. Investigate pricing, service quality and complaints among fiber-optic customers.
6. Monitor high-risk customer segments for targeted retention actions.

## Disclaimer

The results describe patterns and associations in the dataset. They should not be interpreted as proof of causation without further testing.
