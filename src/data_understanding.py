
import pandas as pd

# Load Dataset
df = pd.read_csv("data/raw/smartmess_dataset.csv")

print("=" * 60)
print("SMARTMESS AI - DATA UNDERSTANDING")
print("=" * 60)

# Dataset Shape

print("\nDataset Shape")
print(df.shape)

# First Five Rows

print("\nFirst Five Rows")
print(df.head())

# Last Five Rows

print("\nLast Five Rows")
print(df.tail())

# Column Names

print("\nColumns")

for col in df.columns:
    print(col)

# Data Types

print("\nData Types")

print(df.dtypes)

# Missing Values

print("\nMissing Values")

print(df.isnull().sum())

# Duplicate Rows

print("\nDuplicate Rows")

print(df.duplicated().sum())

# Summary Statistics

print("\nSummary Statistics")

print(df.describe(include="all"))

# Memory Usage


print("\nMemory Usage")

print(df.memory_usage(deep=True))

# Unique Values


print("\nUnique Values")

for column in df.columns:

    print(f"{column} : {df[column].nunique()}")

print("\nData Understanding Completed Successfully.")