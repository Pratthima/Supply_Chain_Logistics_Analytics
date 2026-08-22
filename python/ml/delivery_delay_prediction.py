import pandas as pd

file_path = "data/clean_supply_chain.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nDelivery Status:")
print(df["Delivery_Status"].value_counts())