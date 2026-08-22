import pandas as pd
import numpy as np
import os


# ============================================================
# PHASE 3 - DATA CLEANING & FEATURE ENGINEERING
# ============================================================


print("=" * 70)
print("SUPPLY CHAIN DATA CLEANING")
print("=" * 70)


# ============================================================
# 1. FIND PROJECT DIRECTORY
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# ============================================================
# 2. DEFINE FILE PATHS
# ============================================================

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

INPUT_FILE = os.path.join(
    DATA_DIR,
    "supply_chain.csv"
)

OUTPUT_FILE = os.path.join(
    DATA_DIR,
    "clean_supply_chain.csv"
)


# ============================================================
# 3. CHECK WHETHER DATASET EXISTS
# ============================================================

if not os.path.exists(INPUT_FILE):

    print()
    print("ERROR: Dataset not found!")
    print()
    print("Expected file:")
    print(INPUT_FILE)
    print()

    exit()


# ============================================================
# 4. LOAD DATASET
# ============================================================

print()
print("Loading dataset...")

df = pd.read_csv(
    INPUT_FILE
)

print("Dataset loaded successfully.")


# ============================================================
# 5. ORIGINAL DATASET INFORMATION
# ============================================================

print()
print("-" * 70)
print("ORIGINAL DATASET INFORMATION")
print("-" * 70)

print()

print(
    "Rows:",
    df.shape[0]
)

print(
    "Columns:",
    df.shape[1]
)


# ============================================================
# 6. DISPLAY COLUMN NAMES
# ============================================================

print()
print("Columns:")

for column in df.columns:

    print(
        "-",
        column
    )


# ============================================================
# 7. CHECK DUPLICATE RECORDS
# ============================================================

print()
print("-" * 70)
print("DUPLICATE CHECK")
print("-" * 70)

duplicate_count = df.duplicated().sum()

print(
    "Duplicate rows:",
    duplicate_count
)


# Remove duplicates
if duplicate_count > 0:

    df = df.drop_duplicates()

    print(
        "Duplicates removed:",
        duplicate_count
    )

else:

    print(
        "No duplicate records found."
    )


# ============================================================
# 8. CHECK MISSING VALUES
# ============================================================

print()
print("-" * 70)
print("MISSING VALUE CHECK")
print("-" * 70)

missing_values = df.isnull().sum()

print(
    missing_values
)


total_missing = missing_values.sum()

print()

print(
    "Total missing values:",
    total_missing
)


# ============================================================
# 9. DATA TYPE CONVERSION
# ============================================================

print()
print("-" * 70)
print("CONVERTING DATA TYPES")
print("-" * 70)


# Convert date columns

date_columns = [
    "Order_Date",
    "Expected_Delivery_Date",
    "Actual_Delivery_Date"
]


for column in date_columns:

    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )


# Numeric columns

numeric_columns = [
    "Supplier_Rating",
    "Warehouse_Capacity",
    "Warehouse_Utilization",
    "Quantity",
    "Unit_Price",
    "Order_Value",
    "Distance_KM",
    "Shipping_Cost",
    "Delivery_Delay_Days",
    "Inventory_Level",
    "Reorder_Level"
]


for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


print(
    "Data types converted successfully."
)


# ============================================================
# 10. HANDLE MISSING VALUES
# ============================================================

print()
print("-" * 70)
print("HANDLING MISSING VALUES")
print("-" * 70)


# Numeric columns
for column in numeric_columns:

    if df[column].isnull().sum() > 0:

        df[column] = df[column].fillna(
            df[column].median()
        )


# Text columns
text_columns = df.select_dtypes(
    include=["object"]
).columns


for column in text_columns:

    if df[column].isnull().sum() > 0:

        df[column] = df[column].fillna(
            "Unknown"
        )


print(
    "Missing values handled."
)


# ============================================================
# 11. REMOVE INVALID QUANTITIES
# ============================================================

print()
print("-" * 70)
print("VALIDATING QUANTITIES")
print("-" * 70)


invalid_quantity = (
    df["Quantity"] <= 0
).sum()


print(
    "Invalid quantity records:",
    invalid_quantity
)


if invalid_quantity > 0:

    df = df[
        df["Quantity"] > 0
    ]


# ============================================================
# 12. REMOVE INVALID PRICES
# ============================================================

invalid_price = (
    df["Unit_Price"] <= 0
).sum()


print(
    "Invalid price records:",
    invalid_price
)


if invalid_price > 0:

    df = df[
        df["Unit_Price"] > 0
    ]


# ============================================================
# 13. CREATE DELIVERY DELAY CATEGORY
# ============================================================

print()
print("-" * 70)
print("CREATING DELIVERY DELAY CATEGORY")
print("-" * 70)


def classify_delay(days):

    if days == 0:

        return "On Time"

    elif days <= 3:

        return "Minor Delay"

    elif days <= 7:

        return "Moderate Delay"

    else:

        return "Severe Delay"


df["Delay_Category"] = (
    df["Delivery_Delay_Days"]
    .apply(classify_delay)
)


# ============================================================
# 14. CREATE ORDER MONTH
# ============================================================

df["Order_Month"] = (
    df["Order_Date"]
    .dt.month
)


# ============================================================
# 15. CREATE ORDER MONTH NAME
# ============================================================

df["Order_Month_Name"] = (
    df["Order_Date"]
    .dt.strftime("%B")
)


# ============================================================
# 16. CREATE ORDER QUARTER
# ============================================================

df["Order_Quarter"] = (
    "Q"
    + df["Order_Date"]
    .dt.quarter
    .astype(str)
)


# ============================================================
# 17. CREATE ORDER YEAR
# ============================================================

df["Order_Year"] = (
    df["Order_Date"]
    .dt.year
)


# ============================================================
# 18. CREATE WEEKDAY
# ============================================================

df["Order_Day"] = (
    df["Order_Date"]
    .dt.day_name()
)


# ============================================================
# 19. CREATE SHIPPING COST PER KM
# ============================================================

df["Shipping_Cost_Per_KM"] = (
    df["Shipping_Cost"]
    / df["Distance_KM"]
)


# ============================================================
# 20. CREATE INVENTORY RISK
# ============================================================

def inventory_risk(row):

    inventory = row["Inventory_Level"]

    reorder = row["Reorder_Level"]

    if inventory < reorder:

        return "High Risk"

    elif inventory <= reorder * 1.5:

        return "Medium Risk"

    else:

        return "Low Risk"


df["Inventory_Risk"] = (
    df.apply(
        inventory_risk,
        axis=1
    )
)


# ============================================================
# 21. CREATE WAREHOUSE RISK
# ============================================================

def warehouse_risk(utilization):

    if utilization >= 90:

        return "High Risk"

    elif utilization >= 75:

        return "Medium Risk"

    else:

        return "Low Risk"


df["Warehouse_Risk"] = (
    df["Warehouse_Utilization"]
    .apply(warehouse_risk)
)


# ============================================================
# 22. CREATE DELIVERY RISK
# ============================================================

def delivery_risk(row):

    delay = row["Delivery_Delay_Days"]

    if delay == 0:

        return "Low Risk"

    elif delay <= 3:

        return "Medium Risk"

    else:

        return "High Risk"


df["Delivery_Risk"] = (
    df.apply(
        delivery_risk,
        axis=1
    )
)


# ============================================================
# 23. CREATE OVERALL SUPPLY CHAIN RISK
# ============================================================

def overall_risk(row):

    risk_score = 0


    # Delivery risk
    if row["Delivery_Risk"] == "High Risk":

        risk_score += 40

    elif row["Delivery_Risk"] == "Medium Risk":

        risk_score += 20


    # Inventory risk
    if row["Inventory_Risk"] == "High Risk":

        risk_score += 30

    elif row["Inventory_Risk"] == "Medium Risk":

        risk_score += 15


    # Warehouse risk
    if row["Warehouse_Risk"] == "High Risk":

        risk_score += 30

    elif row["Warehouse_Risk"] == "Medium Risk":

        risk_score += 15


    if risk_score >= 60:

        return "High Risk"

    elif risk_score >= 30:

        return "Medium Risk"

    else:

        return "Low Risk"


df["Overall_Risk"] = (
    df.apply(
        overall_risk,
        axis=1
    )
)


# ============================================================
# 24. ROUND DECIMAL VALUES
# ============================================================

df["Warehouse_Utilization"] = (
    df["Warehouse_Utilization"]
    .round(2)
)


df["Shipping_Cost_Per_KM"] = (
    df["Shipping_Cost_Per_KM"]
    .round(2)
)


# ============================================================
# 25. SORT DATA
# ============================================================

df = df.sort_values(
    by="Order_Date"
)


# ============================================================
# 26. RESET INDEX
# ============================================================

df = df.reset_index(
    drop=True
)


# ============================================================
# 27. FINAL DATASET CHECK
# ============================================================

print()
print("-" * 70)
print("FINAL DATASET INFORMATION")
print("-" * 70)

print()

print(
    "Rows:",
    df.shape[0]
)

print(
    "Columns:",
    df.shape[1]
)


# ============================================================
# 28. CHECK MISSING VALUES AGAIN
# ============================================================

print()
print("Final missing values:")

print(
    df.isnull().sum().sum()
)


# ============================================================
# 29. DISPLAY NEW FEATURES
# ============================================================

print()
print("New features created:")

new_features = [
    "Delay_Category",
    "Order_Month",
    "Order_Month_Name",
    "Order_Quarter",
    "Order_Year",
    "Order_Day",
    "Shipping_Cost_Per_KM",
    "Inventory_Risk",
    "Warehouse_Risk",
    "Delivery_Risk",
    "Overall_Risk"
]


for feature in new_features:

    print(
        "-",
        feature
    )


# ============================================================
# 30. DISPLAY RISK DISTRIBUTION
# ============================================================

print()
print("-" * 70)
print("OVERALL SUPPLY CHAIN RISK")
print("-" * 70)

print(
    df["Overall_Risk"]
    .value_counts()
)


# ============================================================
# 31. SAVE CLEAN DATASET
# ============================================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ============================================================
# 32. FINAL MESSAGE
# ============================================================

print()
print("=" * 70)

print(
    "DATA CLEANING COMPLETED SUCCESSFULLY"
)

print("=" * 70)

print()

print(
    "Clean dataset saved at:"
)

print(
    OUTPUT_FILE
)

print()

print(
    "Final dataset shape:",
    df.shape
)

print()

print(
    "First 5 cleaned records:"
)

print(
    df.head()
)

print()

print("=" * 70)