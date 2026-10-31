# Task 2 – Customer Retention & Churn Analysis

## 1. Objective

Analyze customer data for a subscription-based business to identify churn patterns, retention drivers, customer lifetime trends, and practical actions that can reduce customer loss.

## 2. Dataset

The analysis uses the Telco Customer Churn dataset. After converting `TotalCharges` to numeric and removing 11 rows where the value was missing, **7,032 customers** were analyzed.

## 3. Key Metrics

- **Customers analyzed:** 7,032
- **Overall churn rate:** 26.58%
- **Average tenure of customers who stayed:** 37.65 months
- **Average tenure of customers who churned:** 17.98 months
- **Average monthly charge of customers who stayed:** 61.31
- **Average monthly charge of customers who churned:** 74.44
- **Average total charges of customers who stayed:** 2,555.34
- **Average total charges of customers who churned:** 1,531.80

## 4. Churn Analysis

### Contract Type

| Contract | Churn Rate |
|---|---:|
| Month-to-month | 42.71% |
| One year | 11.28% |
| Two year | 2.85% |

Month-to-month customers show the highest churn rate, while two-year customers show the lowest. This indicates that longer-term contracts are strongly associated with customer retention.

### Customer Tenure

| Tenure | Churn Rate |
|---|---:|
| 0–6 months | 53.33% |
| 7–12 months | 35.89% |
| 13–24 months | 28.71% |
| 25–48 months | 20.39% |
| 49–72 months | 9.51% |

Churn is highest among customers in their first six months and decreases steadily as tenure increases. This makes the early customer lifecycle a major retention opportunity.

### Payment Method

| Payment Method | Churn Rate |
|---|---:|
| Electronic check | 45.29% |
| Mailed check | 19.20% |
| Bank transfer (automatic) | 16.73% |
| Credit card (automatic) | 15.25% |

Customers using electronic checks have substantially higher churn than customers using automatic payment methods.

### Internet Service

| Internet Service | Churn Rate |
|---|---:|
| Fiber optic | 41.89% |
| DSL | 19.00% |
| No internet service | 7.43% |

Fiber-optic customers have a notably higher churn rate than DSL customers. This is an important segment for further investigation because the dataset alone does not establish the reason for the difference.

### Tech Support

| Tech Support | Churn Rate |
|---|---:|
| No | 41.65% |
| Yes | 15.20% |
| No internet service | 7.43% |

Customers without tech support have a much higher churn rate than customers with tech support. This suggests that support access may be an important retention lever.

## 5. Main Insights

1. **Early-tenure customers are the highest-risk segment.** Churn reaches 53.33% during the first 0–6 months.
2. **Contract type is strongly associated with churn.** Month-to-month customers churn at 42.71%, compared with only 2.85% for two-year customers.
3. **Electronic-check users are a high-risk payment segment.** Their churn rate is 45.29%.
4. **Tech support is associated with lower churn.** The churn rate is 15.20% for customers with tech support versus 41.65% without it.
5. **Churned customers have shorter tenure and higher average monthly charges.** The average tenure is 17.98 months for churned customers versus 37.65 months for retained customers; average monthly charges are 74.44 versus 61.31.
6. **Fiber-optic customers have elevated churn.** The 41.89% churn rate makes this segment worth investigating further, although the analysis does not prove that the service itself causes churn.

## 6. Business Recommendations

### 1. Strengthen the first-six-month onboarding program

Create welcome campaigns, setup assistance, proactive support and check-ins during the first six months, when churn risk is highest.

### 2. Encourage longer-term contracts

Offer targeted incentives or value-added benefits to suitable month-to-month customers to encourage one-year or two-year commitments.

### 3. Reduce dependence on high-risk payment behavior

Promote convenient automatic payment options to customers currently using electronic checks, while avoiding aggressive or inappropriate pressure.

### 4. Promote technical support

Offer targeted support trials, onboarding assistance and proactive troubleshooting to customers without tech support.

### 5. Investigate the fiber-optic segment

Compare pricing, service quality, support contacts, outages and customer complaints for fiber-optic customers before deciding on a specific corrective action.

### 6. Build a churn-risk monitoring process

Track high-risk combinations such as low tenure + month-to-month contract + high monthly charges and prioritize them for retention campaigns.

## 7. Conclusion

The analysis shows that customer churn is concentrated in specific segments, especially new customers, month-to-month customers, electronic-check users and customers without tech support. A retention strategy focused on early onboarding, contract migration, support adoption and targeted high-risk monitoring can help reduce customer loss.

> Note: These findings show associations in the dataset. They should be used to prioritize further investigation rather than treated as proof that any single factor directly causes churn.
