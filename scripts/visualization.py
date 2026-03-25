import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs/plots", exist_ok=True)

df = pd.read_csv("data/processed/feature_enriched_dataset.csv")

sample = df[df["commodity"] == df["commodity"].iloc[0]]

plt.figure(figsize=(12,5))

plt.plot(sample["date"], sample["price"])
plt.title("Price Trend")
plt.xticks(sample["date"][::20], rotation=45)

plt.tight_layout()

plt.savefig("outputs/plots/trend.png")
plt.close()

print("visualization created")