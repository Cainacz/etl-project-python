import pandas as pd

def transform_sales(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_", regex=True)
                  .str.replace("%", "percent")
    )

    rename_map = {
        "product_line": "product_category",
        "tax_5percent": "tax_5_percent",
        "sales": "total",
        "rating": "customer_rating",
        "payment": "payment_method",
        "gross_income": "tax_amount",
    }
    df = df.rename(columns=rename_map)


    df["sale_date"] = pd.to_datetime(df["date"], format="%m/%d/%Y", errors="coerce")

 
    df["sale_datetime"] = pd.to_datetime(
        df["date"] + " " + df["time"],
        format="%m/%d/%Y %I:%M:%S %p",
        errors="coerce"
    )


    df["sale_date"] = df["sale_datetime"].dt.date     
    df["sale_time"] = df["sale_datetime"].dt.time      

  
    invalid_datetime = df["sale_datetime"].isna()
    if invalid_datetime.any():
        print(f"{invalid_datetime.sum()} lines with invalid date/hour will be removed")
        df = df[~invalid_datetime]

    numeric_cols = ["quantity", "unit_price", "cogs", "tax_5_percent", "total", "customer_rating"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["profit"] = df["total"] - df["cogs"]
    df["profit_margin"] = (df["profit"] / df["total"].replace(0, pd.NA)).round(4)

    df = df.dropna(subset=["invoice_id", "sale_date", "total", "quantity", "unit_price"])
    df = df.drop_duplicates(subset=["invoice_id"])

    for col in ["product_category", "branch", "city", "customer_type", "gender", "payment_method"]:
        if col in df.columns:
            df[col] = df[col].str.strip().str.title()

    print("Columns after transforming", df.columns.tolist())
    return df