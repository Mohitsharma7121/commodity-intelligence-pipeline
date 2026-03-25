import pandas as pd

df = pd.read_csv("data/processed/cleaned_merged_dataset.csv")

df = df.sort_values(by=["commodity", "date"])

df["price_change_pct"] = df.groupby("commodity")["price"].pct_change()

df["rolling_7"] = df.groupby("commodity")["price"].transform(lambda x: x.rolling(7).mean())
df["rolling_14"] = df.groupby("commodity")["price"].transform(lambda x: x.rolling(14).mean())
df["rolling_30"] = df.groupby("commodity")["price"].transform(lambda x: x.rolling(30).mean())

df["volatility"] = df.groupby("commodity")["price"].transform(lambda x: x.rolling(7).std())

df["trend"] = df["rolling_7"] - df["rolling_30"]

df.to_csv("data/processed/feature_enriched_dataset.csv", index=False)

print("feature engineering complete")