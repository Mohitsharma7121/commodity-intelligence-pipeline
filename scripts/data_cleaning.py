import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

wb = pd.read_csv("data/raw_data/world_bank.csv")
fao = pd.read_csv("data/raw_data/fao.csv")

wb["date"] = pd.to_datetime(wb["date"], errors="coerce")
fao["date"] = pd.to_datetime(fao["date"], errors="coerce")

wb["commodity"] = wb["commodity"].str.lower().str.strip()
fao["commodity"] = fao["commodity"].str.lower().str.strip()

wb["region"] = "global"
wb["source"] = "world_bank"

fao["region"] = "india"
fao["source"] = "fao"

wb = wb[["commodity", "date", "price", "region", "source"]]
fao = fao[["commodity", "date", "price", "region", "source"]]

df = pd.concat([wb, fao], ignore_index=True)

df = df.sort_values(by=["commodity", "date"])

df.to_csv("data/processed/cleaned_merged_dataset.csv", index=False)

print("cleaning complete")