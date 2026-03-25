import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs/plots", exist_ok=True)

df = pd.read_csv("data/processed/feature_enriched_dataset.csv")

sample = df[df["commodity"] == df["commodity"].iloc[0]]

# -------------------
# 1. PRICE TREND
# -------------------
plt.figure(figsize=(12,5))
plt.plot(sample["date"], sample["price"])
plt.title("Price Trend")
plt.xticks(sample["date"][::20], rotation=45)
plt.tight_layout()
plt.savefig("outputs/plots/price_trend.png")
plt.close()


# -------------------
# 2. MOVING AVERAGES
# -------------------
plt.figure(figsize=(12,5))
plt.plot(sample["date"], sample["rolling_7"], label="MA 7")
plt.plot(sample["date"], sample["rolling_14"], label="MA 14")
plt.plot(sample["date"], sample["rolling_30"], label="MA 30")

plt.title("Moving Averages")
plt.legend()
plt.xticks(sample["date"][::20], rotation=45)
plt.tight_layout()
plt.savefig("outputs/plots/moving_averages.png")
plt.close()


# -------------------
# 3. VOLATILITY
# -------------------
plt.figure(figsize=(12,5))
plt.plot(sample["date"], sample["volatility"])

plt.title("Volatility (7-day std)")
plt.xticks(sample["date"][::20], rotation=45)
plt.tight_layout()
plt.savefig("outputs/plots/volatility.png")
plt.close()


print("all visualizations created")
