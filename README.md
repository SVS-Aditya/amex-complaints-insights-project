# Amex Customer Complaints Insights Project

This end-to-end data analytics project simulates how American Express can analyze customer complaints to drive actionable insights, reduce escalations, and improve customer experience. Built using real-world public CFPB complaint data, it includes sentiment analysis, churn and escalation prediction modeling, BigQuery integration, and an interactive Power BI dashboard.

> **Disclaimer**: This is an educational/portfolio project. It is not affiliated with or endorsed by American Express. The data used is publicly available from the Consumer Financial Protection Bureau (CFPB).

---

## Business Context

American Express operates in a highly competitive, customer-centric environment. Understanding **customer complaints**, **sentiments**, and **escalation risks** is vital for:
- Enhancing service quality
- Reducing regulatory risk
- Improving retention
- Strengthening customer advocacy

This project aligns with real-world job functions like:
- Performance Management
- Complaints Reporting & Insights
- Risk & Fraud Analytics
- Customer Listening & Sentiment Analysis

---

## Key Highlights

| Module                      | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Data Cleaning           | Cleaned and preprocessed 6M+ complaint records from CFPB                    |
| Text Analytics          | NLP on complaint narratives + VADER sentiment scoring                       |
| ML Models               | Built churn and escalation prediction models (Random Forest, Logistic)     |
| BigQuery Integration   | Uploaded cleaned sentiment data to Google BigQuery + analytical SQL queries |
| Power BI Dashboard      | Built interactive dashboard with 5 key business visuals                     |

---

## Project Structure
<pre> <code> ```bash amex-complaints-insights-project/ ├── data/ # Final cleaned dataset with sentiment ├── notebooks/ # Jupyter notebooks for each pipeline step ├── outputs/ # Models, predictions, and exports ├── dashboard/ # Power BI dashboard files (.pbix + PDF) ├── scripts/ # Optional scripts for simulated automation └── README.md # You're here! ``` </code> </pre>
## Power BI Dashboard Overview

Visuals included:
- Monthly Complaint Trends
- Top 10 Complaint Issues
- Sentiment Breakdown by Issue
- Timely vs Non-Timely Responses (Grouped)
- Channel Distribution (Donut Chart)
  <img width="1920" height="1080" alt="Screenshot (37)" src="https://github.com/user-attachments/assets/cad06788-bdeb-422b-af87-d0468914d870" />
The dashboard was built using **Power BI (PBIX)** and exported as **PDF** for easy viewing.

## Machine Learning Models

### Churn Prediction Model
- Target: Whether a complaint led to customer churn
- Features: Sentiment score, channel, issue, etc.
- Model: Logistic Regression
- Output: `churn_model.pkl` + predictions CSV

### Escalation Risk Model
- Target: Whether a complaint was disputed (escalated)
- Model: Random Forest
- Output: `escalation_model.pkl` + predictions

Both models include evaluation metrics and were saved for future integration.

## Tools & Skills Demonstrated

- **Python**: pandas, scikit-learn, matplotlib, seaborn, nltk, vaderSentiment
- **SQL / BigQuery**: Cloud-native querying and insights
- **NLP**: Text preprocessing, sentiment classification
- **Power BI**: Data modeling + interactive dashboard
- **Cloud**: Google Cloud CLI, BigQuery authentication
- **Version Control**: Git + GitHub
- **Soft Skills**: Business framing, metric design, problem-solving

---

## Project Goals

Simulate real-world responsibilities in roles like:
- MIS & Advanced Analytics
- Customer Listening & Complaint Insights
- Servicing Risk / Fraud Analytics
- Performance Management & CX Ops

Deliver end-to-end pipeline:
From raw public data → business-ready dashboard & predictions.

---

## Data Source

- **CFPB Consumer Complaint Database**  
  [https://www.consumerfinance.gov/data-research/consumer-complaints/](https://www.consumerfinance.gov/data-research/consumer-complaints/)

- **Customer Churn Dataset**  
  [https://www.kaggle.com/datasets/blastchar/telco-customer-churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)


## License

This project is for academic and portfolio use only.  
All data used is public domain.


