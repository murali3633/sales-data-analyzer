# Sales Data Analyzer (Superstore Dataset)
# Project: Analyze sales data CSV to find top products, revenue, and monthly trends
# Tools: Python, Pandas, Matplotlib
# Relevance: Demonstrates Python skills for data analysis, useful for roles like IBM ASE or Data Analyst

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the sales data CSV
df = pd.read_csv('sales_data.csv', encoding='latin1')

# Step 2: Basic overview
print("First 5 rows of data:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

# Step 3: Use 'Sales' column as revenue
df['Revenue'] = df['Sales']

# Step 4: Total revenue overall
total_revenue = df['Revenue'].sum()
print(f"\nTotal Revenue: ${total_revenue:.2f}")

# Step 5: Top 5 products by revenue
top_products = df.groupby('Product Name')['Revenue'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products by Revenue:")
print(top_products)

# Step 6: Monthly trends
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Revenue'].sum()
print("\nMonthly Revenue:")
print(monthly_revenue)

# Step 7: Visualizations

# Top Products Bar Chart
plt.figure(figsize=(10,6))
top_products.plot(kind='bar', color='skyblue')
plt.title("Top 5 Products by Revenue")
plt.ylabel("Revenue ($)")
plt.xlabel("Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Monthly Revenue Line Chart
plt.figure(figsize=(10,6))
monthly_revenue.plot(marker='o', linestyle='-', color='green')
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue ($)")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 8: Optional - Save analysis results
top_products.to_csv('top_products.csv')
monthly_revenue.to_csv('monthly_revenue.csv')
print("\nAnalysis saved to CSV files: top_products.csv, monthly_revenue.csv")
