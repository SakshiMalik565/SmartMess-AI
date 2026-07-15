import pandas as pd


def fill_rainfall(df):
    """
    Fill missing rainfall values based on weather conditions.
    """
    if "Weather" in df.columns and "Rainfall" in df.columns:

        # Sunny means no rainfall
        df.loc[
            (df["Weather"] == "Sunny") & (df["Rainfall"].isna()),
            "Rainfall"
        ] = 0

        # Remaining rainfall → median by weather
        df["Rainfall"] = (
            df.groupby("Weather")["Rainfall"]
            .transform(lambda x: x.fillna(x.median()))
        )

    return df


def fill_humidity(df):
    """
    Fill humidity using Weather + Season groups.
    """
    if "Humidity" in df.columns:

        df["Humidity"] = (
            df.groupby(["Weather", "Season"])["Humidity"]
            .transform(lambda x: x.fillna(x.median()))
        )

    return df


def fill_supplier_delay(df):
    """
    Missing supplier delay means no delay.
    """
    if "SupplierDelay" in df.columns:

        df["SupplierDelay"] = df["SupplierDelay"].fillna(0)

    return df


def fill_meal_rating(df):
    """
    Fill AverageMealRating using FoodQualityScore.
    """

    if (
        "AverageMealRating" in df.columns
        and "FoodQualityScore" in df.columns
    ):

        median_rating = df["AverageMealRating"].median()

        df["AverageMealRating"] = df["AverageMealRating"].fillna(
            median_rating
        )

    return df


def fill_food_quality(df):

    if "FoodQualityScore" in df.columns:

        df["FoodQualityScore"] = df["FoodQualityScore"].fillna(
            df["FoodQualityScore"].median()
        )

    return df


def fill_utilities(df):
    """
    Estimate Electricity, Water and Gas
    using TotalMealsServed.
    """

    attendance = "TotalAttendance"

    if attendance not in df.columns:
        return df

    if "ElectricityConsumption" in df.columns:

        estimate = 40 + df[attendance] * 0.05

        df["ElectricityConsumption"] = (
            df["ElectricityConsumption"]
            .fillna(estimate)
        )

    if "WaterConsumption" in df.columns:

        estimate = 500 + df[attendance] * 1.2

        df["WaterConsumption"] = (
            df["WaterConsumption"]
            .fillna(estimate)
        )

    if "GasConsumption" in df.columns:

        estimate = 15 + df[attendance] * 0.02

        df["GasConsumption"] = (
            df["GasConsumption"]
            .fillna(estimate)
        )

    return df