"""
validation.py

Generates a data quality report after cleaning.
"""

import pandas as pd


def validate_dataset(df):
    """
    Print dataset quality report.
    """

    print("\n" + "=" * 60)
    print("SMARTMESS AI - DATA QUALITY REPORT")
    print("=" * 60)

    print(f"\nRows               : {df.shape[0]}")
    print(f"Columns            : {df.shape[1]}")

    # -----------------------------
    # Missing Values
    # -----------------------------

    missing = df.isnull().sum()

    print("\nMissing Values")

    if missing.sum() == 0:
        print("No missing values found.")
    else:
        print(missing[missing > 0])

    # -----------------------------
    # Duplicate Rows
    # -----------------------------

    duplicates = df.duplicated().sum()

    print("\nDuplicate Rows")

    print(duplicates)

    # -----------------------------
    # Negative Inventory
    # -----------------------------

    inventory_cols = [
        "InventoryRice",
        "InventoryDal",
        "InventoryVegetables",
        "InventoryMilk"
    ]

    print("\nInventory Validation")

    for col in inventory_cols:

        if col in df.columns:

            invalid = (df[col] < 0).sum()

            print(f"{col}: {invalid} invalid rows")

    # -----------------------------
    # Food Validation
    # -----------------------------

    food_items = [
        ("RiceCookedKg", "RiceConsumedKg"),
        ("DalCookedKg", "DalConsumedKg"),
        ("VegetableCookedKg", "VegetableConsumedKg"),
        ("ChapatiPrepared", "ChapatiConsumed")
    ]

    print("\nFood Quantity Validation")

    for cooked, consumed in food_items:

        if cooked in df.columns and consumed in df.columns:

            invalid = (df[consumed] > df[cooked]).sum()

            print(f"{consumed} > {cooked}: {invalid}")

    # -----------------------------
    # Financial Validation
    # -----------------------------

    financial = [
        "DailyOperatingCost",
        "DailyRevenue"
    ]

    print("\nFinancial Validation")

    for col in financial:

        if col in df.columns:

            invalid = (df[col] < 0).sum()

            print(f"{col}: {invalid}")

    print("\nDataset Validation Completed Successfully.")

    print("=" * 60)