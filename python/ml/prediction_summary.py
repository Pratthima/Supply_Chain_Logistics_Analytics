import pandas as pd
import os

# Input dataset
input_file = "data/clean_supply_chain.csv"

# Output file
output_file = "reports/ml/prediction_summary.csv"

# Load dataset
df = pd.read_csv(input_file)

# Calculate summary values
total_orders = len(df)

delayed_orders = (df["Delivery_Status"] == "Delayed").sum()

on_time_orders = (df["Delivery_Status"] == "On Time").sum()

delay_rate = (delayed_orders / total_orders) * 100

average_delay = df["Delivery_Delay_Days"].mean()

# Create summary table
summary = pd.DataFrame({
    "Metric": [
        "Total Orders",
        "Delayed Orders",
        "On Time Orders",
        "Delay Rate (%)",
        "Average Delay Days"
    ],
    "Value": [
        total_orders,
        delayed_orders,
        on_time_orders,
        round(delay_rate, 2),
        round(average_delay, 2)
    ]
})

# Make sure output folder exists
os.makedirs("reports/ml", exist_ok=True)

# Save summary
summary.to_csv(output_file, index=False)

print("\nPrediction summary created successfully!")
print("\nSummary:")
print(summary)

print(f"\nSaved to: {output_file}")