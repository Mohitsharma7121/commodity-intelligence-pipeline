import pandas as pd

df = pd.read_csv("data/processed/cleaned_merged_dataset.csv")

print("Missing values:\n", df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())
print("\nDate type:", df["date"].dtype)
print("\nPrice summary:\n", df["price"].describe())

assert df["price"].isnull().sum() == 0
assert df["commodity"].isnull().sum() == 0

print("\nvalidation complete")