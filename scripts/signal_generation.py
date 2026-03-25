import pandas as pd
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("data/processed/feature_enriched_dataset.csv")

signals = []

for _, row in df.iterrows():

    signal = None

    if row["price_change_pct"] > 0.05:
        signal = "demand rising"

    elif row["price_change_pct"] < -0.05:
        signal = "price falling"

    elif row["volatility"] > 2:
        signal = "high volatility"

    elif row["trend"] > 0:
        signal = "uptrend"

    if signal:
        signals.append({
            "commodity": row["commodity"],
            "signal": signal,
            "confidence": round(abs(row["price_change_pct"]), 2),
            "timestamp": row["date"]
        })

signals_df = pd.DataFrame(signals)

signals_df.to_csv("outputs/signals.csv", index=False)

print("signal generation complete")