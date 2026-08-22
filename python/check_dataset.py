import pandas as pd

file_path = "../data/supply_chain.csv"

df = pd.read_csv(file_path)

print("\n========== DATASET CHECK ==========\n")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDelivery status:")
print(df["Delivery_Status"].value_counts())

print("\nInventory status:")
print(df["Inventory_Status"].value_counts())

print("\nShipping mode:")
print(df["Shipping_Mode"].value_counts())

print("\nProduct categories:")
print(df["Product_Category"].value_counts())

print("\n====================================")