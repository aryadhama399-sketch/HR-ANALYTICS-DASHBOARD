# HR Analytics Dashboard — Kinetrexa Data Analytics Internship

## Project Overview
An interactive HR analytics solution built with Python and Power BI to analyze employee attrition, workforce characteristics, salary patterns, job roles, overtime, satisfaction, and business travel.

## Internship Task
This project addresses **Task 3: HR Analytics Dashboard** from the Kinetrexa Software Private Limited Data Analytics Internship assignment.

Required deliverables include a public GitHub repository, source code/SQL scripts, Power BI/Tableau dashboard, README documentation, and HR Analytics Report (PDF).

## Dashboard Pages
1. **HR Analytics Dashboard** — executive KPIs and attrition overview
2. **Attrition Analysis** — age, satisfaction, work-life balance, and distance analysis
3. **Workforce & Salary** — department workforce, income, salary hike and performance
4. **Job Role Analysis** — employee count, attrition, income and tenure by role

## Key KPIs
- Total Employees: **1,470**
- Attrition Count: **237**
- Attrition Rate: **16.12%**
- Average Age: **36.9 years**
- Average Monthly Income: **~$6,503**
- Average Years at Company: **~7.0 years**

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Power BI
- DAX

## Repository Structure
```text
HR-Analytics-Internship/
├── PowerBI/
│   └── HR_Analytics_Dashboard.pbix
├── Data/
│   └── HR_Employee_Attrition.csv
├── Notebook/
│   └── HR_Analytics.ipynb
├── Reports/
│   └── HR_Analytics_Report.pdf
├── Screenshots/
├── src/
│   └── analysis.py
├── requirements.txt
└── README.md
```

## Important Data Limitation
The supplied HR dataset contains no attendance-related field. Therefore, attendance metrics were **not fabricated**. Attendance analysis would require a separate verified attendance dataset.

## How to Run the Python Analysis
```bash
pip install -r requirements.txt
python src/analysis.py
```

## Power BI
Open `PowerBI/HR_Analytics_Dashboard.pbix` in Power BI Desktop. The report contains the interactive dashboard, DAX measures, synced slicers, and page navigation.

## Business Purpose
The dashboard helps HR teams identify attrition patterns, compare departments and job roles, evaluate overtime and satisfaction factors, and understand workforce and salary trends for data-driven decision-making.
