import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/HR_Employee_Attrition_Cleaned.csv")

print("Dataset shape:", df.shape)
print("\nAttrition counts:")
print(df["Attrition"].value_counts())

attrition_rate = (df["Attrition"].eq("Yes").mean()) * 100
print(f"\nAttrition rate: {attrition_rate:.2f}%")

print("\nDepartment summary:")
dept = df.groupby("Department").agg(
    Employees=("EmployeeNumber","count"),
    Attrition_Count=("Attrition", lambda x: x.eq("Yes").sum()),
    Avg_Monthly_Income=("MonthlyIncome","mean")
)
dept["Attrition_Rate_%"] = dept["Attrition_Count"] / dept["Employees"] * 100
print(dept.sort_values("Attrition_Rate_%", ascending=False))

print("\nOvertime attrition:")
print(df.groupby("OverTime")["Attrition"].apply(lambda x: x.eq("Yes").mean()*100))
