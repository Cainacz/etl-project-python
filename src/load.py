import sqlite3
import pandas as pd

def load_dimensions_and_get_ids(df: pd.DataFrame, db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()


    cities = df["city"].dropna().unique()
    for city in cities:
        cursor.execute("INSERT OR IGNORE INTO city (city) VALUES (?)", (city,))
    conn.commit()


    products = df["product_category"].dropna().unique()
    for prod in products:
        cursor.execute("INSERT OR IGNORE INTO product_line (product_category) VALUES (?)", (prod,))
    conn.commit()


    branch_city = df[["branch", "city"]].drop_duplicates().dropna()
    for _, row in branch_city.iterrows():
        cursor.execute("SELECT city_id FROM city WHERE city = ?", (row["city"],))
        city_id = cursor.fetchone()
        if city_id:
            cursor.execute(
                """
                INSERT OR IGNORE INTO branch (branch_name, city_id)
                VALUES (?, ?)
                """,
                (row["branch"], city_id[0])
            )
    conn.commit()

    city_map = pd.read_sql("SELECT city_id, city FROM city", conn).set_index("city")["city_id"]
    df["city_id_temp"] = df["city"].map(city_map)


    branch_df = pd.read_sql("SELECT branch_id, branch_name, city_id FROM branch", conn)
    branch_map = branch_df.set_index(["branch_name", "city_id"])["branch_id"]
    df["branch_id"] = df.apply(
        lambda row: branch_map.get((row["branch"], row["city_id_temp"]), None), axis=1
    )


    product_map = pd.read_sql("SELECT product_id, product_category FROM product_line", conn)\
                    .set_index("product_category")["product_id"]
    df["product_id"] = df["product_category"].map(product_map)

    conn.close()

    return df

def load_to_sqlite(df_clean: pd.DataFrame, db_path: str):

    df_with_ids = load_dimensions_and_get_ids(df_clean, db_path)


    columns_for_sales = [
        "invoice_id",
        "sale_date",
        "sale_time",
        "product_id",
        "branch_id",
        "customer_type",
        "gender",
        "payment_method",
        "quantity",
        "unit_price",
        "cogs",
        "tax_5_percent",
        "total",
        "profit",
        "profit_margin",
        "customer_rating"
    ]


    existing_cols = [c for c in columns_for_sales if c in df_with_ids.columns]
    df_db = df_with_ids[existing_cols]


    missing = df_db[df_db[["product_id", "branch_id"]].isna().any(axis=1)]
    if not missing.empty:
        print(f"{len(missing)} lines without product_id or branch_id will be ignored")
        df_db = df_db[["product_id", "branch_id"]].dropna()


    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sales")
    conn.commit() 

    conn = sqlite3.connect(db_path)
    df_db.to_sql("sales", conn, if_exists="append", index=False)
    conn.close()

    print(f"Loaded {len(df_db)} sales on the table sales.")

