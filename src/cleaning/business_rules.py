import pandas as pd


def validate_food_quantities(df):
    """
    Ensure:
    Consumed <= Cooked
    Waste = Cooked - Consumed
    """

    food_items = [
        ("RiceCookedKg", "RiceConsumedKg", "RiceWasteKg"),
        ("DalCookedKg", "DalConsumedKg", "DalWasteKg"),
        ("VegetableCookedKg", "VegetableConsumedKg", "VegetableWasteKg"),
        ("ChapatiPrepared", "ChapatiConsumed", "ChapatiWaste")
    ]

    for cooked, consumed, waste in food_items:

        if cooked in df.columns and consumed in df.columns:

            # Consumed can never exceed cooked
            df.loc[df[consumed] > df[cooked], consumed] = df[cooked]

            # Waste = Cooked - Consumed
            if waste in df.columns:
                df[waste] = df[cooked] - df[consumed]

                # Waste cannot be negative
                df.loc[df[waste] < 0, waste] = 0

    return df


def validate_inventory(df):
    """
    Inventory can never be negative.
    """

    inventory_columns = [
        "InventoryRice",
        "InventoryDal",
        "InventoryVegetables",
        "InventoryMilk"
    ]

    for col in inventory_columns:

        if col in df.columns:

            df.loc[df[col] < 0, col] = 0

    return df


def validate_attendance(df):
    """
    Attendance should never exceed registered students.
    """

    attendance_columns = [
        "BreakfastAttendance",
        "LunchAttendance",
        "DinnerAttendance"
    ]

    if "StudentsRegistered" not in df.columns:
        return df

    for col in attendance_columns:

        if col in df.columns:

            df.loc[
                df[col] > df["StudentsRegistered"],
                col
            ] = df["StudentsRegistered"]

    return df


def validate_cost_and_revenue(df):
    """
    Cost and Revenue should never be negative.
    """

    financial_columns = [
        "DailyOperatingCost",
        "DailyRevenue"
    ]

    for col in financial_columns:

        if col in df.columns:

            df.loc[df[col] < 0, col] = 0

    return df


def recalculate_waste_percentage(df):
    """
    Waste Percentage =
    WasteKg / Total Food Prepared
    """

    required = [
        "RiceCookedKg",
        "DalCookedKg",
        "VegetableCookedKg",
        "WasteKg",
        "WastePercentage"
    ]

    if not all(col in df.columns for col in required):
        return df

    total_prepared = (
        df["RiceCookedKg"] +
        df["DalCookedKg"] +
        df["VegetableCookedKg"]
    )

    total_prepared = total_prepared.replace(0, 1)

    df["WastePercentage"] = (
        df["WasteKg"] /
        total_prepared
    ) * 100

    return df


def classify_waste(df):
    """
    Create WasteCategory using WastePercentage.
    """

    if "WastePercentage" not in df.columns:
        return df

    df["WasteCategory"] = pd.cut(
        df["WastePercentage"],
        bins=[-1, 5, 12, 100],
        labels=["Low", "Medium", "High"]
    )

    return df