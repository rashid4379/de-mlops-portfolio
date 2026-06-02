import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

raw_file = RAW_DIR / "orders.csv"
clean_file = PROCESSED_DIR / "orders_clean.csv"

sample_data = {
    "order_id": [1, 2, 3, 4, 5, 6],
    "customer_id": [101, 102, 101, 103, 102, None],
    "order_date": [
        "2024-01-01",
        "2024-01-02",
        "2024-01-04",
        "2024-01-05",
        "2024-01-07",
        "2024-01-08",
    ],
    "amount": [120.00, 250.00, 300.00, 90.00, 400.00, None],
}

df = pd.DataFrame(sample_data)
df.to_csv(raw_file, index=False)

print("Raw data saved to:", raw_file)

df = pd.read_csv(raw_file)

print("\nRaw data preview:")
print(df)

df = df.dropna(subset=["order_id", "customer_id", "order_date", "amount"])

df["order_id"] = df["order_id"].astype(int)
df["customer_id"] = df["customer_id"].astype(int)
df["order_date"] = pd.to_datetime(df["order_date"])
df["amount"] = df["amount"].astype(float)

df = df.drop_duplicates(subset=["order_id"])

df.to_csv(clean_file, index=False)

print("\nClean data preview:")
print(df)

print("\nClean data saved to:", clean_file)
print("ETL completed successfully.")