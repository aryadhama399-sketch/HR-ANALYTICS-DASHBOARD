# HR Analytics Dashboard

A data analytics project based on the HR Employee Attrition dataset.

## Objective
Analyze employee demographics, attrition, salary, job roles, departments, overtime and workforce characteristics to support HR decision-making.

## Dataset
- Rows: 1,470
- Columns: 35
- Target: `Attrition`
- Source file used: `WA_Fn-UseC_-HR-Employee-Attrition.csv`

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Power BI
- GitHub

## Key KPIs
- Total Employees: 1,470
- Attrition Count: 237
- Attrition Rate: 16.12%
- Average Age: 36.9
- Average Monthly Income: $6,503
- Average Years at Company: 7.0

## Dashboard Pages
1. Executive Overview
2. Attrition Analysis
3. Workforce & Salary Analysis
4. Job Role / Department Analysis

## Important Data Limitation
The dataset does not contain an attendance column, so attendance analysis is not possible from this file without adding another verified data source.

## Project Structure
- `data/` — cleaned data and summary tables
- `images/` — analysis charts
- `reports/` — business insights
- `dashboard/` — Power BI/DAX guide
- `notebooks/` — notebook
- `src/` — reusable analysis script

## How to Run
```bash
pip install -r requirements.txt
python src/analysis.py
```
