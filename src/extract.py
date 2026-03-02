import pandas as pd
from pathlib import Path



def extract_from_csv(csv_path: str | Path) -> pd.DataFrame:
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    df = pd.read_csv(csv_path)

    print("Extract step completed")
    print(f"Rows: {len(df)} | Columns: {list(df.columns)}")

    return df