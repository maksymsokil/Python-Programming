import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Explore structure
print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())

# Clean data
df = df.drop_duplicates()
df = df.dropna()

# Make sure date is treated as a date
df["Date"] = pd.to_datetime(df["Date"])

# Create month column
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# Summary statistics
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()

print("\nTotal Sales:", total_sales)
print("Average Sale Amount:", average_sales)

# Grouping and analysis
sales_by_category = df.groupby("Category")["Sales"].sum()
sales_by_month = df.groupby("Month")["Sales"].sum()

print("\nSales by Category:")
print(sales_by_category)

print("\nSales by Month:")
print(sales_by_month)

# Visualization 1: Bar chart
sales_by_category.plot(kind="bar", title="Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization 2: Line chart
sales_by_month.plot(kind="line", marker="o", title="Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()