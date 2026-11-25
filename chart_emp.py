import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")


avg_salary = df.groupby("department")["salary"].mean()
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(avg_salary.index, avg_salary.values, color="steelblue")
ax.bar_label(bars, fmt="%.0f")
ax.set_title("Average Salary per Department")
ax.set_xlabel("Department")
ax.set_ylabel("Average Salary")
plt.tight_layout()
plt.savefig("bar_avg_salary.png", dpi=150)
plt.close()


fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["salary"], bins=5, color="seagreen", edgecolor="black")
ax.set_title("Salary Distribution")
ax.set_xlabel("Salary")
ax.set_ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("histogram_salary.png", dpi=150)
plt.close()


fig, ax = plt.subplots(figsize=(8, 5))
for dept, group in df.groupby("department"):
    ax.scatter(group["id"], group["salary"], label=dept)
ax.set_title("Employee ID vs Salary by Department")
ax.set_xlabel("Employee ID")
ax.set_ylabel("Salary")
ax.legend(title="Department")
plt.tight_layout()
plt.savefig("scatter_id_salary.png", dpi=150)
plt.close()


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(months, sales, marker="o", color="darkorange")
ax.set_title("Monthly Sales (Jan - Jun)")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
plt.tight_layout()
plt.savefig("line_monthly_sales.png", dpi=150)
plt.close()

print("Done! Saved 4 PNG files.")