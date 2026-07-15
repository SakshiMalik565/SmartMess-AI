"""
SmartMess AI

Main Data Cleaning Pipeline
"""

import pandas as pd
from pathlib import Path

# Cleaning Modules
from cleaning.missing_values import (
    fill_rainfall,
    fill_humidity,
    fill_supplier_delay,
    fill_food_quality,
    fill_meal_rating,
    fill_utilities
)

from cleaning.business_rules import (
    validate_food_quantities,
    validate_inventory,
    validate_attendance,
    validate_cost_and_revenue,
    recalculate_waste_percentage,
    classify_waste
)

from cleaning.validation import validate_dataset


# ---------------------------------------------------
# Paths
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw" / "smartmess_dataset.csv"

PROCESSED_DATA = (
    BASE_DIR
    / "data"
    / "processed"
    / "smartmess_cleaned.csv"
)


# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

print("\nLoading Dataset...")

df = pd.read_csv(RAW_DATA)

print("Dataset Loaded Successfully.")


# ---------------------------------------------------
# Convert Date
# ---------------------------------------------------

if "Date" in df.columns:

    df["Date"] = pd.to_datetime(df["Date"])


# ---------------------------------------------------
# Missing Values
# ---------------------------------------------------

print("\nHandling Missing Values...")

df = fill_rainfall(df)
df = fill_humidity(df)
df = fill_supplier_delay(df)
df = fill_food_quality(df)
df = fill_meal_rating(df)
df = fill_utilities(df)

print("Missing Values Handled.")


# ---------------------------------------------------
# Business Rules
# ---------------------------------------------------

print("\nApplying Business Rules...")

df = validate_food_quantities(df)
df = validate_inventory(df)
df = validate_attendance(df)
df = validate_cost_and_revenue(df)
df = recalculate_waste_percentage(df)
df = classify_waste(df)

print("Business Rules Applied.")


# ---------------------------------------------------
# Remove Duplicates
# ---------------------------------------------------

duplicates = df.duplicated().sum()

if duplicates > 0:

    print(f"\nRemoving {duplicates} duplicate rows...")

    df = df.drop_duplicates()

else:

    print("\nNo Duplicate Rows Found.")


# ---------------------------------------------------
# Validation Report
# ---------------------------------------------------

validate_dataset(df)


# ---------------------------------------------------
# Save Clean Dataset
# ---------------------------------------------------

PROCESSED_DATA.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(PROCESSED_DATA, index=False)

print("\nCleaned Dataset Saved Successfully!")

print(PROCESSED_DATA)