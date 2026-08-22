import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("data/clean_supply_chain.csv")

# Create output folder
os.makedirs("reports/ml/charts", exist_ok=True)

# --------------------------------------------------
# 1. Delivery Status Distribution
# --------------------------------------------------

status = df["Delivery_Status"].value_counts()

plt.figure(figsize=(8, 5))
status.plot(kind="bar")

plt.title("Delivery Status Distribution")
plt.xlabel("Delivery Status")
plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig(
    "reports/ml/charts/delivery_status_ml.png",
    dpi=300
)

plt.close()


# --------------------------------------------------
# 2. Delivery Delay Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

df["Delivery_Delay_Days"].hist(bins=20)

plt.title("Delivery Delay Distribution")
plt.xlabel("Delay Days")
plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig(
    "reports/ml/charts/delay_distribution.png",
    dpi=300
)

plt.close()


# --------------------------------------------------
# 3. Distance vs Delivery Delay
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Distance_KM"],
    df["Delivery_Delay_Days"],
    alpha=0.4
)

plt.title("Distance vs Delivery Delay")
plt.xlabel("Distance (KM)")
plt.ylabel("Delay Days")

plt.tight_layout()

plt.savefig(
    "reports/ml/charts/distance_vs_delay.png",
    dpi=300
)

plt.close()


print("\nML visualizations created successfully!")

print("\nCreated files:")
print("1. delivery_status_ml.png")
print("2. delay_distribution.png")
print("3. distance_vs_delay.png")