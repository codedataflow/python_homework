import sqlite3
import pandas as pd

# 1) Connect to the database and read data into a DataFrame

with sqlite3.connect("../db/lesson.db") as conn:

    query = """
    SELECT 
        line_items.line_item_id,
        line_items.quantity,
        products.product_id,
        products.product_name,
        products.price
    FROM line_items
    JOIN products
        ON line_items.product_id = products.product_id
    """

    df = pd.read_sql_query(query, conn)

# 2) Print first 5 lines of the original DataFrame
print("\n=== First 5 rows (raw data) ===")
print(df.head())

# 3) Add 'total' column (quantity * price)
df["total"] = df["quantity"] * df["price"]

print("\n=== First 5 rows (with total column) ===")
print(df.head())

# 4) Group by product_id and aggregate
summary_df = (
    df
    .groupby("product_id")
    .agg({
        "line_item_id": "count",
        "total": "sum",
        "product_name": "first"
    })
)

print("\n=== First 5 rows after groupby/agg ===")
print(summary_df.head())

# 5) Sort by product_name
summary_df = summary_df.sort_values(by="product_name")

# 6) Write to CSV
output_path = "order_summary.csv"
summary_df.to_csv(output_path)

print(f"\nFile written successfully to: {output_path}")
