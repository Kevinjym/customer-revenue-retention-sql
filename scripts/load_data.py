
from pathlib import Path
import pandas as pd

# 1. Locate project files
project_dir = Path(__file__).resolve().parent.parent

input_file = project_dir / "data/raw/Online Retail.xlsx"
output_file = project_dir / "data/processed/online_retail.csv"

# 2. Read original Excel dataset
df = pd.read_excel(
    input_file,
    engine="openpyxl",
    dtype={
        "InvoiceNo": "string",
        "StockCode": "string",
        "CustomerID": "Int64"
    }
)

# 3. Inspect data
print("Dataset shape:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isna().sum())

print("\nFirst 5 rows:")
print(df.head())

# 4. Rename columns to match PostgreSQL
df = df.rename(columns={
    "InvoiceNo": "invoice_no",
    "StockCode": "stock_code",
    "Description": "description",
    "Quantity": "quantity",
    "InvoiceDate": "invoice_date",
    "UnitPrice": "unit_price",
    "CustomerID": "customer_id",
    "Country": "country"
})

# 5. Validate column names
expected_columns = [
    "invoice_no",
    "stock_code",
    "description",
    "quantity",
    "invoice_date",
    "unit_price",
    "customer_id",
    "country"
]

assert df.columns.tolist() == expected_columns, \
    "Column names do not match the expected schema."

assert len(df) == 541909, \
    "Unexpected number of rows. Check the source file."

# 6. Export CSV
output_file.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8",
    date_format="%Y-%m-%d %H:%M:%S"
)

print("\nCSV export completed!")
print("File:", output_file)
print("Exported rows:", len(df))
