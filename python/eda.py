import pandas as pd
import matplotlib.pyplot as plt
import os


# ============================================================
# PHASE 4 - EXPLORATORY DATA ANALYSIS
# ============================================================

print("=" * 70)
print("SUPPLY CHAIN - EXPLORATORY DATA ANALYSIS")
print("=" * 70)


# ============================================================
# 1. PROJECT DIRECTORIES
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_DIR = os.path.join(BASE_DIR, "data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
CHART_DIR = os.path.join(REPORT_DIR, "charts")
ANALYSIS_DIR = os.path.join(REPORT_DIR, "analysis")


os.makedirs(CHART_DIR, exist_ok=True)
os.makedirs(ANALYSIS_DIR, exist_ok=True)


# ============================================================
# 2. DATASET
# ============================================================

INPUT_FILE = os.path.join(
    DATA_DIR,
    "clean_supply_chain.csv"
)

if not os.path.exists(INPUT_FILE):
    print()
    print("ERROR: clean_supply_chain.csv was not found.")
    print()
    print("Expected location:")
    print(INPUT_FILE)
    exit()


# ============================================================
# 3. LOAD DATA
# ============================================================

print()
print("Loading cleaned dataset...")

df = pd.read_csv(INPUT_FILE)

print("Dataset loaded successfully.")


# ============================================================
# 4. CONVERT DATES
# ============================================================

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"]
)

df["Expected_Delivery_Date"] = pd.to_datetime(
    df["Expected_Delivery_Date"]
)

df["Actual_Delivery_Date"] = pd.to_datetime(
    df["Actual_Delivery_Date"]
)


# ============================================================
# 5. BASIC INFORMATION
# ============================================================

print()
print("-" * 70)
print("BASIC DATASET INFORMATION")
print("-" * 70)

print()
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Total Orders:", df["Order_ID"].nunique())


# ============================================================
# 6. KEY KPIs
# ============================================================

print()
print("-" * 70)
print("KEY BUSINESS KPIs")
print("-" * 70)


total_orders = df["Order_ID"].nunique()

total_quantity = df["Quantity"].sum()

total_revenue = df["Order_Value"].sum()

total_shipping_cost = df["Shipping_Cost"].sum()

average_order_value = df["Order_Value"].mean()

average_shipping_cost = df["Shipping_Cost"].mean()

average_delay = df["Delivery_Delay_Days"].mean()


on_time_orders = (
    df["Delivery_Status"] == "On Time"
).sum()

delayed_orders = (
    df["Delivery_Status"] == "Delayed"
).sum()


on_time_percentage = (
    on_time_orders / total_orders
) * 100

delay_percentage = (
    delayed_orders / total_orders
) * 100


print()
print(f"Total Orders: {total_orders:,}")
print(f"Total Quantity: {total_quantity:,}")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Shipping Cost: ₹{total_shipping_cost:,.2f}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Average Shipping Cost: ₹{average_shipping_cost:,.2f}")
print(f"Average Delivery Delay: {average_delay:.2f} days")
print(f"On-Time Delivery: {on_time_percentage:.2f}%")
print(f"Delayed Shipments: {delay_percentage:.2f}%")


# ============================================================
# 7. DELIVERY ANALYSIS
# ============================================================

print()
print("-" * 70)
print("DELIVERY ANALYSIS")
print("-" * 70)


delivery_analysis = (
    df["Delivery_Status"]
    .value_counts()
)

print()
print(delivery_analysis)


# ============================================================
# 8. SHIPPING MODE ANALYSIS
# ============================================================

print()
print("-" * 70)
print("SHIPPING MODE ANALYSIS")
print("-" * 70)


shipping_analysis = (
    df.groupby("Shipping_Mode")
    .agg(
        Shipments=("Order_ID", "count"),
        Total_Cost=("Shipping_Cost", "sum"),
        Average_Cost=("Shipping_Cost", "mean"),
        Average_Delay=("Delivery_Delay_Days", "mean")
    )
    .sort_values(
        "Shipments",
        ascending=False
    )
)

print()
print(shipping_analysis)


# ============================================================
# 9. SUPPLIER ANALYSIS
# ============================================================

print()
print("-" * 70)
print("SUPPLIER PERFORMANCE")
print("-" * 70)


supplier_analysis = (
    df.groupby(
        [
            "Supplier_ID",
            "Supplier_Name"
        ]
    )
    .agg(
        Orders=("Order_ID", "count"),
        Average_Rating=("Supplier_Rating", "mean"),
        Average_Delay=("Delivery_Delay_Days", "mean"),
        Shipping_Cost=("Shipping_Cost", "sum"),
        Revenue=("Order_Value", "sum")
    )
    .sort_values(
        "Average_Delay"
    )
)

print()
print(supplier_analysis)


# ============================================================
# 10. WAREHOUSE ANALYSIS
# ============================================================

print()
print("-" * 70)
print("WAREHOUSE PERFORMANCE")
print("-" * 70)


warehouse_analysis = (
    df.groupby(
        [
            "Warehouse_ID",
            "Warehouse_Name"
        ]
    )
    .agg(
        Orders=("Order_ID", "count"),
        Average_Utilization=(
            "Warehouse_Utilization",
            "mean"
        ),
        Total_Inventory=(
            "Inventory_Level",
            "sum"
        ),
        Average_Delay=(
            "Delivery_Delay_Days",
            "mean"
        )
    )
    .sort_values(
        "Average_Utilization",
        ascending=False
    )
)

print()
print(warehouse_analysis)


# ============================================================
# 11. PRODUCT ANALYSIS
# ============================================================

print()
print("-" * 70)
print("PRODUCT PERFORMANCE")
print("-" * 70)


product_analysis = (
    df.groupby(
        [
            "Product_ID",
            "Product_Name",
            "Product_Category"
        ]
    )
    .agg(
        Orders=("Order_ID", "count"),
        Quantity=("Quantity", "sum"),
        Revenue=("Order_Value", "sum"),
        Average_Price=("Unit_Price", "mean"),
        Average_Inventory=(
            "Inventory_Level",
            "mean"
        )
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)

print()
print(product_analysis.head(10))


# ============================================================
# 12. MONTHLY ANALYSIS
# ============================================================

print()
print("-" * 70)
print("MONTHLY ORDER ANALYSIS")
print("-" * 70)


monthly_analysis = (
    df.groupby(
        [
            "Order_Year",
            "Order_Month"
        ]
    )
    .agg(
        Orders=("Order_ID", "count"),
        Revenue=("Order_Value", "sum"),
        Shipping_Cost=("Shipping_Cost", "sum"),
        Average_Delay=("Delivery_Delay_Days", "mean")
    )
    .reset_index()
)


monthly_analysis["Month"] = (
    monthly_analysis["Order_Year"].astype(str)
    + "-"
    + monthly_analysis["Order_Month"]
    .astype(str)
    .str.zfill(2)
)


print()
print(monthly_analysis)


# ============================================================
# 13. INVENTORY ANALYSIS
# ============================================================

print()
print("-" * 70)
print("INVENTORY ANALYSIS")
print("-" * 70)


inventory_analysis = (
    df["Inventory_Status"]
    .value_counts()
)

inventory_risk_analysis = (
    df["Inventory_Risk"]
    .value_counts()
)


print()
print("Inventory Status:")
print(inventory_analysis)

print()
print("Inventory Risk:")
print(inventory_risk_analysis)


# ============================================================
# 14. OVERALL RISK
# ============================================================

print()
print("-" * 70)
print("SUPPLY CHAIN RISK ANALYSIS")
print("-" * 70)


risk_analysis = (
    df["Overall_Risk"]
    .value_counts()
)

print()
print(risk_analysis)


# ============================================================
# 15. DESTINATION ANALYSIS
# ============================================================

print()
print("-" * 70)
print("DESTINATION DELAY ANALYSIS")
print("-" * 70)


destination_analysis = (
    df.groupby("Destination")
    .agg(
        Shipments=("Order_ID", "count"),
        Average_Delay=("Delivery_Delay_Days", "mean"),
        Delayed_Shipments=(
            "Delivery_Status",
            lambda x: (x == "Delayed").sum()
        )
    )
    .sort_values(
        "Average_Delay",
        ascending=False
    )
)


print()
print(destination_analysis)


# ============================================================
# FUNCTION TO SAVE CHART
# ============================================================

def save_current_chart(filename):

    plt.tight_layout()

    output_path = os.path.join(
        CHART_DIR,
        filename
    )

    plt.savefig(
        output_path,
        dpi=150,
        bbox_inches="tight"
    )

    plt.close()


# ============================================================
# CHART 1 - DELIVERY STATUS
# ============================================================

plt.figure(figsize=(8, 6))

plt.bar(
    delivery_analysis.index,
    delivery_analysis.values
)

plt.title(
    "Delivery Status Distribution"
)

plt.xlabel(
    "Delivery Status"
)

plt.ylabel(
    "Number of Shipments"
)

save_current_chart(
    "01_delivery_status.png"
)


# ============================================================
# CHART 2 - SHIPPING MODE
# ============================================================

plt.figure(figsize=(8, 6))

plt.bar(
    shipping_analysis.index,
    shipping_analysis["Shipments"]
)

plt.title(
    "Shipments by Shipping Mode"
)

plt.xlabel(
    "Shipping Mode"
)

plt.ylabel(
    "Number of Shipments"
)

save_current_chart(
    "02_shipping_mode.png"
)


# ============================================================
# CHART 3 - SHIPPING COST
# ============================================================

plt.figure(figsize=(8, 6))

plt.bar(
    shipping_analysis.index,
    shipping_analysis["Total_Cost"]
)

plt.title(
    "Total Shipping Cost by Mode"
)

plt.xlabel(
    "Shipping Mode"
)

plt.ylabel(
    "Shipping Cost"
)

save_current_chart(
    "03_shipping_cost.png"
)


# ============================================================
# CHART 4 - SUPPLIER DELAY
# ============================================================

supplier_chart = (
    supplier_analysis[
        "Average_Delay"
    ]
    .sort_values(
        ascending=False
    )
)


plt.figure(figsize=(10, 6))

plt.bar(
    supplier_chart.index.get_level_values(
        "Supplier_Name"
    ),
    supplier_chart.values
)

plt.title(
    "Average Delivery Delay by Supplier"
)

plt.xlabel(
    "Supplier"
)

plt.ylabel(
    "Average Delay (Days)"
)

plt.xticks(
    rotation=45,
    ha="right"
)

save_current_chart(
    "04_supplier_delay.png"
)


# ============================================================
# CHART 5 - WAREHOUSE UTILIZATION
# ============================================================

warehouse_chart = (
    warehouse_analysis[
        "Average_Utilization"
    ]
)


plt.figure(figsize=(10, 6))

plt.bar(
    warehouse_chart.index.get_level_values(
        "Warehouse_Name"
    ),
    warehouse_chart.values
)

plt.title(
    "Warehouse Utilization"
)

plt.xlabel(
    "Warehouse"
)

plt.ylabel(
    "Utilization (%)"
)

plt.xticks(
    rotation=45,
    ha="right"
)

save_current_chart(
    "05_warehouse_utilization.png"
)


# ============================================================
# CHART 6 - TOP PRODUCTS
# ============================================================

top_products = (
    product_analysis
    .head(10)
)


plt.figure(figsize=(10, 6))

plt.bar(
    top_products.index.get_level_values(
        "Product_Name"
    ),
    top_products["Revenue"]
)

plt.title(
    "Top 10 Products by Revenue"
)

plt.xlabel(
    "Product"
)

plt.ylabel(
    "Revenue"
)

plt.xticks(
    rotation=45,
    ha="right"
)

save_current_chart(
    "06_top_products_revenue.png"
)


# ============================================================
# CHART 7 - MONTHLY REVENUE
# ============================================================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_analysis["Month"],
    monthly_analysis["Revenue"],
    marker="o"
)

plt.title(
    "Monthly Revenue Trend"
)

plt.xlabel(
    "Month"
)

plt.ylabel(
    "Revenue"
)

plt.xticks(
    rotation=45
)

save_current_chart(
    "07_monthly_revenue.png"
)


# ============================================================
# CHART 8 - INVENTORY STATUS
# ============================================================

plt.figure(figsize=(8, 6))

plt.bar(
    inventory_analysis.index,
    inventory_analysis.values
)

plt.title(
    "Inventory Status"
)

plt.xlabel(
    "Inventory Status"
)

plt.ylabel(
    "Number of Records"
)

plt.xticks(
    rotation=0
)

save_current_chart(
    "08_inventory_status.png"
)


# ============================================================
# CHART 9 - OVERALL RISK
# ============================================================

plt.figure(figsize=(8, 6))

plt.bar(
    risk_analysis.index,
    risk_analysis.values
)

plt.title(
    "Overall Supply Chain Risk"
)

plt.xlabel(
    "Risk Level"
)

plt.ylabel(
    "Number of Records"
)

plt.xticks(
    rotation=0
)

save_current_chart(
    "09_overall_risk.png"
)


# ============================================================
# CHART 10 - DELAY CATEGORY
# ============================================================

delay_category = (
    df["Delay_Category"]
    .value_counts()
)


plt.figure(figsize=(8, 6))

plt.bar(
    delay_category.index,
    delay_category.values
)

plt.title(
    "Delivery Delay Category"
)

plt.xlabel(
    "Delay Category"
)

plt.ylabel(
    "Number of Shipments"
)

plt.xticks(
    rotation=30
)

save_current_chart(
    "10_delay_category.png"
)


# ============================================================
# SAVE ANALYSIS TABLES
# ============================================================

supplier_analysis.to_csv(
    os.path.join(
        ANALYSIS_DIR,
        "supplier_analysis.csv"
    )
)

warehouse_analysis.to_csv(
    os.path.join(
        ANALYSIS_DIR,
        "warehouse_analysis.csv"
    )
)

product_analysis.to_csv(
    os.path.join(
        ANALYSIS_DIR,
        "product_analysis.csv"
    )
)

shipping_analysis.to_csv(
    os.path.join(
        ANALYSIS_DIR,
        "shipping_analysis.csv"
    )
)

monthly_analysis.to_csv(
    os.path.join(
        ANALYSIS_DIR,
        "monthly_analysis.csv"
    ),
    index=False
)

destination_analysis.to_csv(
    os.path.join(
        ANALYSIS_DIR,
        "destination_analysis.csv"
    )
)


# ============================================================
# FINAL OUTPUT
# ============================================================

print()
print("=" * 70)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 70)

print()

print(
    "Charts saved in:"
)

print(
    CHART_DIR
)

print()

print(
    "Analysis tables saved in:"
)

print(
    ANALYSIS_DIR
)

print()

print(
    "Total charts created: 10"
)

print()

print(
    "Total analysis tables created: 6"
)

print()
print("=" * 70)