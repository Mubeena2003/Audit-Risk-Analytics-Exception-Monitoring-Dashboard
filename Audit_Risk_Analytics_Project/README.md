# Audit Risk Analytics & Data Quality Project

## Overview
A synthetic audit analytics project designed to demonstrate how data analytics can support audit and assurance activities.

The project performs:
- Data quality validation
- High-value transaction testing
- Approval/control exception testing
- Duplicate transaction testing
- Rule-based risk scoring
- Exception reporting
- Audit summary reporting

> **Important:** All data in this repository is synthetic and created for portfolio/learning purposes. It is not real client or financial data.

## Business Problem
Audit teams often need to analyze large transaction populations to identify unusual transactions and control exceptions. This project demonstrates a simple, transparent analytics approach that can be extended to real audit datasets.

## Analytics Approach

`Raw Transactions`
→ `Data Quality Checks`
→ `Audit Test Rules`
→ `Risk Scoring`
→ `Exception Identification`
→ `Summary Reporting`

## Audit Tests

### 1. High-Value Transaction Test
Flags transactions above a defined threshold of 100,000.

### 2. Approval Exception Test
Flags transactions where approval status is "No".

### 3. Duplicate Transaction Test
Flags repeated combinations of vendor, transaction date, and amount.

### 4. Risk Scoring
- High-value transaction = 3 points
- Approval exception = 3 points
- Duplicate pattern = 2 points

Risk levels:
- 0 = Low
- 1–2 = Medium
- 3+ = High

## Tech Stack
- Python
- Pandas
- NumPy
- CSV
- Data Quality Checks
- Data Wrangling
- Audit Analytics
- Risk Assessment
- Exception Analysis

## Project Structure

```text
PwC_Audit_Risk_Analytics_Project/
│
├── data/
│   └── transactions.csv
│
├── src/
│   └── audit_analysis.py
│
├── outputs/
│   ├── audit_exceptions.csv
│   ├── audit_summary.csv
│   └── data_quality_summary.csv
│
├── requirements.txt
└── README.md
```

## How to Run

```bash
pip install -r requirements.txt
python src/audit_analysis.py
```

The analysis generates three output files inside the `outputs` folder.

## Skills Demonstrated
- Data wrangling
- Data validation
- Data quality analysis
- Exception identification
- Risk assessment
- Rule-based audit testing
- Business process understanding
- Python-based analytics
- Structured reporting

## Future Enhancements
- Add SQL-based analysis
- Build a Power BI audit risk dashboard
- Add statistical anomaly detection
- Add automated email alerts for high-risk exceptions
- Add Alteryx workflow equivalent
- Add additional internal-control test cases
