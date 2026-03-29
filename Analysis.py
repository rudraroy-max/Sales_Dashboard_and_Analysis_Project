import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='latin-1')

# First look
print(df.shape)        # How many rows & columns?
print(df.head())       # First 5 rows
print(df.dtypes)       # Data types of each column

# Check for missing values
print(df.isnull().sum())

# Check for duplicates
print("Duplicates:", df.duplicated().sum())

# Convert dates from string to proper datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date']  = pd.to_datetime(df['Ship Date'])

# Extract useful time columns
df['Order Year']  = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Month Name'] = df['Order Date'].dt.strftime('%b')  # Jan, Feb...

# Create a shipping duration column (how many days to ship?)
df['Ship Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# Quick check
print(df[['Order Date', 'Order Year', 'Order Month', 'Ship Days']].head())

# Overview of numeric columns
print(df[['Sales', 'Profit', 'Discount', 'Quantity']].describe().round(2))

# Unique values in key columns
print("Regions:", df['Region'].unique())
print("Categories:", df['Category'].unique())
print("Segments:", df['Segment'].unique())

# Saving the cleaned CSV
df.to_csv("superstore_clean.csv", index=False)
print("Cleaned file saved!")

# We'll answer 5 key business questions using Python and pandas:

# 1 — Total Revenue, Profit & Orders (KPIs)
total_sales    = df['Sales'].sum()
total_profit   = df['Profit'].sum()
total_orders   = df['Order ID'].nunique()
profit_margin  = (total_profit / total_sales) * 100

print(f"Total Sales:    ${total_sales:,.2f}")
print(f"Total Profit:   ${total_profit:,.2f}")
print(f"Profit Margin:  {profit_margin:.2f}%")
print(f"Total Orders:   {total_orders}")

# 2 — Sales ,Profit & Order by Region
region_summary = df.groupby('Region').agg(
    Total_Sales   = ('Sales', 'sum'),
    Total_Profit  = ('Profit', 'sum'),
    Total_Orders  = ('Order ID', 'nunique')
).round(2).sort_values('Total_Sales', ascending=False)

print(region_summary)

# 3 — Top 10 Best-Selling Products
top_products = df.groupby('Product Name').agg(
    Total_Sales  = ('Sales', 'sum'),
    Total_Profit = ('Profit', 'sum')
).sort_values('Total_Sales', ascending=False).head(10)

print(top_products)

# 4 — Monthly Sales Trend (which months perform best?)
monthly_sales = df.groupby(['Order Year', 'Order Month', 'Order Month Name']).agg(
    Sales  = ('Sales', 'sum'),
    Profit = ('Profit', 'sum')
).reset_index().sort_values(['Order Year', 'Order Month'])

print(monthly_sales)

# 5 — Category & Sub-Category Performance
category_summary = df.groupby(['Category', 'Sub-Category']).agg(
    Total_Sales   = ('Sales', 'sum'),
    Total_Profit  = ('Profit', 'sum'),
    Avg_Discount  = ('Discount', 'mean')
).round(2).sort_values('Total_Profit', ascending=False)

print(category_summary)

# 6 — Loss-Making Sub-Categories (important insight)
losses = category_summary[category_summary['Total_Profit'] < 0]
print("Sub-categories running at a LOSS:")
print(losses)