import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier

# Load dataset
input_file = "data/clean_supply_chain.csv"
df = pd.read_csv(input_file)

# Features used for prediction
features = [
    "Distance_KM",
    "Shipping_Cost",
    "Quantity",
    "Unit_Price",
    "Warehouse_Utilization",
    "Inventory_Level",
    "Reorder_Level",
    "Supplier_Rating"
]

# Check that all required columns exist
missing_columns = [col for col in features if col not in df.columns]

if missing_columns:
    print("Missing columns:")
    print(missing_columns)
    raise SystemExit

# Input features
X = df[features]

# Prediction target
y = (df["Delivery_Status"] == "Delayed").astype(int)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X, y)

# Calculate feature importance
importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

# Sort from highest to lowest
importance = importance.sort_values(
    by="Importance",
    ascending=False
)

# Create output folder
os.makedirs("reports/ml", exist_ok=True)

# Save results
output_file = "reports/ml/feature_importance.csv"

importance.to_csv(
    output_file,
    index=False
)

print("\nFeature Importance:")
print(importance)

print("\nFeature importance file created successfully!")
print(f"Saved to: {output_file}")