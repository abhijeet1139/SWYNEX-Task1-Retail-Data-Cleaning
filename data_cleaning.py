import pandas as pd

df = pd.read_csv("data/raw/retail_store_sales_raw.csv")

# Standardize whitespace
for c in df.select_dtypes("object"):
    df[c] = df[c].map(lambda x: x.strip() if isinstance(x, str) else x)

# Convert numeric fields
for c in ["Price Per Unit", "Quantity", "Total Spent"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# Reconstruct values only when mathematically determinable
df["Price Per Unit"] = df["Price Per Unit"].fillna(
    df["Total Spent"] / df["Quantity"]
)
df["Quantity"] = df["Quantity"].fillna(
    df["Total Spent"] / df["Price Per Unit"]
).round(0)
df["Total Spent"] = df["Total Spent"].fillna(
    df["Price Per Unit"] * df["Quantity"]
)

# Handle categorical missing values
df["Item"] = df["Item"].fillna("Unknown")
df["Discount Applied"] = df["Discount Applied"].fillna("Unknown")

df["Discount Applied"] = df["Discount Applied"].replace({
    "true": "Yes", "false": "No",
    "True": "Yes", "False": "No",
    "TRUE": "Yes", "FALSE": "No",
    "yes": "Yes", "no": "No"
})

# Convert date
df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"], errors="coerce"
)

# Remove rows that cannot be reconstructed
df = df.loc[
    ~(df["Quantity"].isna() & df["Total Spent"].isna())
].copy()

# Remove exact duplicates
df = df.drop_duplicates().reset_index(drop=True)

# Final recoverable totals
df["Total Spent"] = df["Total Spent"].fillna(
    df["Price Per Unit"] * df["Quantity"]
)

df.to_csv(
    "data/cleaned/retail_store_sales_cleaned.csv",
    index=False,
    date_format="%Y-%m-%d"
)

print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Remaining missing values:", int(df.isna().sum().sum()))
print("Remaining exact duplicates:", int(df.duplicated().sum()))
