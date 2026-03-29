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