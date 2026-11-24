import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

avg_salary = df.groupby("department")["salary"].mean()

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(avg_salary.index, avg_salary.values, color="steelblue", edgecolor="black")

ax.set_title("Average Salary per Department")
ax.set_xlabel("Department")
ax.set_ylabel("Average Salary")
ax.bar_label(bars, fmt="%.2f", padding=3)  # Adds exact values on top of each bar

plt.tight_layout()
plt.savefig("avg_salary_by_dept.png", dpi=300)
plt.close()

plt.figure(figsize=(8, 5))
plt.hist(df["salary"], bins=5, color="mediumseagreen", edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("salary_histogram.png", dpi=300)
plt.close()

plt.figure(figsize=(8, 5))

for dept, group in df.groupby("department"):
    plt.scatter(group["id"], group["salary"], label=dept, s=60, alpha=0.8)

plt.title("Employee ID vs. Salary by Department")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")

plt.tight_layout()
plt.savefig("id_vs_salary_scatter.png", dpi=300)
plt.close()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o", linestyle="-", color="coral", linewidth=2)

plt.title("Monthly Sales (Jan – Jun)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("monthly_sales_line.png", dpi=300)
plt.close()

print("All 4 charts saved successfully.")