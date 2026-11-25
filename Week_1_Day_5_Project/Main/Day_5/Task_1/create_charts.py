import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "figures")
os.makedirs(OUT, exist_ok=True)
df = pd.read_csv(os.path.join(BASE, "employee_data.csv"))
sns.set_theme(style="whitegrid")
blue, orange, green = "#4472C4", "#ED7D31", "#70AD47"

# 1. Department bar chart
dep_counts = df["Department"].value_counts()
plt.figure(figsize=(8, 5)); dep_counts.plot(kind="bar", color=blue)
plt.title("Employee Count by Department"); plt.xlabel("Department"); plt.ylabel("Employees (count)"); plt.xticks(rotation=0); plt.tight_layout()
plt.savefig(os.path.join(OUT, "bar_chart.png"), dpi=300); plt.close()

# 2. Salary histogram
plt.figure(figsize=(8, 5)); plt.hist(df["Salary"], bins=5, color=orange, edgecolor="black")
plt.title("Employee Salary Distribution"); plt.xlabel("Monthly Salary (INR)"); plt.ylabel("Employees (count)"); plt.tight_layout()
plt.savefig(os.path.join(OUT, "histogram.png"), dpi=300); plt.close()

# 3. Age vs salary scatter
plt.figure(figsize=(8, 5)); plt.scatter(df["Age"], df["Salary"], color=blue, alpha=.8, label="Employees")
plt.title("Age vs Salary Analysis"); plt.xlabel("Age (years)"); plt.ylabel("Monthly Salary (INR)"); plt.legend(); plt.tight_layout()
plt.savefig(os.path.join(OUT, "scatter_plot.png"), dpi=300); plt.close()

# 4. Monthly hiring line chart
df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])
monthly = df.groupby(df["JoiningDate"].dt.to_period("M")).size(); monthly.index = monthly.index.astype(str)
plt.figure(figsize=(9, 5)); plt.plot(monthly.index, monthly.values, marker="o", color=blue, label="Employees joined")
plt.title("Monthly Employee Joining Trend"); plt.xlabel("Month"); plt.ylabel("New joiners (count)"); plt.xticks(rotation=45); plt.legend(); plt.tight_layout()
plt.savefig(os.path.join(OUT, "line_chart.png"), dpi=300); plt.close()

# 5. Department salary boxplot
plt.figure(figsize=(8, 5)); sns.boxplot(data=df, x="Department", y="Salary", color=green)
plt.title("Salary Comparison Across Departments"); plt.xlabel("Department"); plt.ylabel("Monthly Salary (INR)"); plt.tight_layout()
plt.savefig(os.path.join(OUT, "box_plot.png"), dpi=300); plt.close()
print("Saved all five charts to", OUT)
