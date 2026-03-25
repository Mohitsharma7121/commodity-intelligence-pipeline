import pandas as pd
import os

os.makedirs("data/raw_data", exist_ok=True)

df1 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

df1 = df1.rename(columns={
    "Date": "date",
    "AAPL.Close": "price"
})

df1["commodity"] = "apple"
df1 = df1[["commodity", "date", "price"]]

df1.to_csv("data/raw_data/world_bank.csv", index=False)


df2 = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/MarketArrivals.csv")

df2.columns = df2.columns.str.strip().str.lower()

df2 = df2.rename(columns={
    "market": "commodity",
    "pricemod": "price"
})

df2["date"] = pd.to_datetime(df2["date"], errors="coerce")

df2 = df2[["commodity", "date", "price"]]

df2.to_csv("data/raw_data/fao.csv", index=False)

print("ingestion complete")