import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta


# ============================================================
# SUPPLY CHAIN DATASET GENERATOR
# ============================================================

np.random.seed(42)
random.seed(42)

NUM_RECORDS = 10000


# ============================================================
# MASTER DATA
# ============================================================

products = [
    ("P001", "Laptop", "Electronics"),
    ("P002", "Desktop PC", "Electronics"),
    ("P003", "Monitor", "Electronics"),
    ("P004", "Keyboard", "Accessories"),
    ("P005", "Mouse", "Accessories"),
    ("P006", "Printer", "Office Equipment"),
    ("P007", "Scanner", "Office Equipment"),
    ("P008", "Router", "Networking"),
    ("P009", "Switch", "Networking"),
    ("P010", "Hard Drive", "Storage"),
    ("P011", "SSD", "Storage"),
    ("P012", "RAM", "Computer Parts"),
    ("P013", "Graphics Card", "Computer Parts"),
    ("P014", "Webcam", "Accessories"),
    ("P015", "Headset", "Accessories")
]


suppliers = [
    ("SUP001", "TechSource India", 4.6),
    ("SUP002", "Global Electronics", 4.2),
    ("SUP003", "Prime Components", 4.8),
    ("SUP004", "NextGen Supplies", 3.9),
    ("SUP005", "SmartTech Distributors", 4.4),
    ("SUP006", "Reliable Components", 4.7),
    ("SUP007", "Digital Supply Co", 3.8),
    ("SUP008", "FutureTech Suppliers", 4.5)
]


warehouses = [
    ("WH001", "Chennai Central", "Chennai", 10000),
    ("WH002", "Bangalore Hub", "Bangalore", 12000),
    ("WH003", "Hyderabad Hub", "Hyderabad", 9000),
    ("WH004", "Mumbai Central", "Mumbai", 15000),
    ("WH005", "Delhi Distribution", "Delhi", 14000),
    ("WH006", "Pune Warehouse", "Pune", 8000)
]


shipping_modes = [
    "Road",
    "Rail",
    "Air",
    "Sea"
]


origins = [
    "Chennai",
    "Bangalore",
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Pune"
]


destinations = [
    "Chennai",
    "Bangalore",
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Pune",
    "Kolkata",
    "Ahmedabad",
    "Coimbatore",
    "Jaipur"
]


# ============================================================
# PRODUCT PRICE
# ============================================================

product_prices = {
    "P001": 65000,
    "P002": 55000,
    "P003": 18000,
    "P004": 1500,
    "P005": 800,
    "P006": 12000,
    "P007": 9000,
    "P008": 5000,
    "P009": 7500,
    "P010": 6000,
    "P011": 7000,
    "P012": 3500,
    "P013": 45000,
    "P014": 4000,
    "P015": 2500
}


# ============================================================
# CREATE RECORDS
# ============================================================

records = []

start_date = datetime(2025, 1, 1)


for i in range(1, NUM_RECORDS + 1):

    # --------------------------------------------------------
    # ORDER INFORMATION
    # --------------------------------------------------------

    order_id = f"ORD{i:05d}"

    order_date = start_date + timedelta(
        days=random.randint(0, 364)
    )

    product_id, product_name, category = random.choice(
        products
    )

    supplier_id, supplier_name, supplier_rating = random.choice(
        suppliers
    )

    (
        warehouse_id,
        warehouse_name,
        warehouse_location,
        warehouse_capacity
    ) = random.choice(warehouses)

    quantity = random.randint(1, 100)

    unit_price = product_prices[product_id]

    order_value = quantity * unit_price


    # --------------------------------------------------------
    # SHIPPING INFORMATION
    # --------------------------------------------------------

    shipping_mode = random.choice(shipping_modes)

    origin = random.choice(origins)

    destination = random.choice(destinations)

    # Avoid same origin and destination
    while destination == origin:
        destination = random.choice(destinations)

    distance_km = random.randint(50, 2500)


    # Shipping cost
    if shipping_mode == "Air":
        shipping_rate = 18

    elif shipping_mode == "Road":
        shipping_rate = 8

    elif shipping_mode == "Rail":
        shipping_rate = 5

    else:
        shipping_rate = 3


    shipping_cost = distance_km * shipping_rate


    # --------------------------------------------------------
    # DELIVERY INFORMATION
    # --------------------------------------------------------

    if shipping_mode == "Air":

        expected_days = random.randint(1, 4)

    elif shipping_mode == "Road":

        expected_days = random.randint(3, 8)

    elif shipping_mode == "Rail":

        expected_days = random.randint(5, 12)

    else:

        expected_days = random.randint(10, 20)


    expected_delivery_date = (
        order_date +
        timedelta(days=expected_days)
    )


    # --------------------------------------------------------
    # DELAY PROBABILITY
    # --------------------------------------------------------

    delay_probability = 0.15


    # Lower supplier rating = higher delay
    if supplier_rating < 4.0:

        delay_probability += 0.12

    elif supplier_rating < 4.3:

        delay_probability += 0.05


    # Air is generally faster
    if shipping_mode == "Air":

        delay_probability -= 0.05


    # Long distance = higher delay risk
    if distance_km > 1500:

        delay_probability += 0.08


    # Keep probability between 5% and 60%
    delay_probability = max(
        0.05,
        min(delay_probability, 0.60)
    )


    # Decide delayed or on time
    is_delayed = random.random() < delay_probability


    if is_delayed:

        delay_days = random.randint(1, 10)

        actual_delivery_date = (
            expected_delivery_date +
            timedelta(days=delay_days)
        )

        delivery_status = "Delayed"

    else:

        early_or_late = random.choice([
            0,
            0,
            0,
            1
        ])

        actual_delivery_date = (
            expected_delivery_date +
            timedelta(days=early_or_late)
        )

        delivery_status = "On Time"


    # --------------------------------------------------------
    # INVENTORY
    # --------------------------------------------------------

    inventory_level = random.randint(
        20,
        1000
    )

    reorder_level = random.randint(
        100,
        300
    )


    if inventory_level < reorder_level:

        inventory_status = "Reorder Required"

    else:

        inventory_status = "Sufficient"


    # --------------------------------------------------------
    # WAREHOUSE UTILIZATION
    # --------------------------------------------------------

    warehouse_utilization = random.uniform(
        45,
        98
    )


    # --------------------------------------------------------
    # DELIVERY DELAY
    # --------------------------------------------------------

    delivery_delay_days = max(
        0,
        (
            actual_delivery_date -
            expected_delivery_date
        ).days
    )


    # --------------------------------------------------------
    # CREATE RECORD
    # --------------------------------------------------------

    record = {

        "Order_ID": order_id,

        "Order_Date": order_date.strftime(
            "%Y-%m-%d"
        ),

        "Product_ID": product_id,

        "Product_Name": product_name,

        "Product_Category": category,

        "Supplier_ID": supplier_id,

        "Supplier_Name": supplier_name,

        "Supplier_Rating": supplier_rating,

        "Warehouse_ID": warehouse_id,

        "Warehouse_Name": warehouse_name,

        "Warehouse_Location": warehouse_location,

        "Warehouse_Capacity": warehouse_capacity,

        "Warehouse_Utilization": round(
            warehouse_utilization,
            2
        ),

        "Quantity": quantity,

        "Unit_Price": unit_price,

        "Order_Value": order_value,

        "Shipping_Mode": shipping_mode,

        "Origin": origin,

        "Destination": destination,

        "Distance_KM": distance_km,

        "Shipping_Cost": round(
            shipping_cost,
            2
        ),

        "Expected_Delivery_Date":
            expected_delivery_date.strftime(
                "%Y-%m-%d"
            ),

        "Actual_Delivery_Date":
            actual_delivery_date.strftime(
                "%Y-%m-%d"
            ),

        "Delivery_Status": delivery_status,

        "Delivery_Delay_Days":
            delivery_delay_days,

        "Inventory_Level":
            inventory_level,

        "Reorder_Level":
            reorder_level,

        "Inventory_Status":
            inventory_status
    }


    records.append(record)


# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(records)


# ============================================================
# FIND PROJECT DIRECTORY
# ============================================================

# __file__ = python/generate_dataset.py
# dirname(__file__) = python
# dirname(dirname(__file__)) = project root

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# ============================================================
# CREATE DATA DIRECTORY
# ============================================================

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

os.makedirs(
    DATA_DIR,
    exist_ok=True
)


# ============================================================
# SAVE DATASET
# ============================================================

output_file = os.path.join(
    DATA_DIR,
    "supply_chain.csv"
)


df.to_csv(
    output_file,
    index=False
)


# ============================================================
# DISPLAY RESULTS
# ============================================================

print()
print("=" * 60)
print("SUPPLY CHAIN DATASET CREATED SUCCESSFULLY")
print("=" * 60)

print()

print(
    "Number of records:",
    len(df)
)

print(
    "Number of columns:",
    len(df.columns)
)

print()

print("Delivery Status:")
print(
    df["Delivery_Status"].value_counts()
)

print()

print("Inventory Status:")
print(
    df["Inventory_Status"].value_counts()
)

print()

print("Shipping Mode:")
print(
    df["Shipping_Mode"].value_counts()
)

print()

print("Dataset saved successfully at:")

print(
    output_file
)

print()

print("First 5 records:")

print(
    df.head()
)

print()

print("=" * 60)