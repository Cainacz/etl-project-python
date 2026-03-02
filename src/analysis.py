import sqlite3
import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path.cwd().parent
DB_PATH = PROJECT_ROOT / "data" / "database" / "sales.db"
SQL_FOLDER = PROJECT_ROOT / "sql" / "analysis"

def run_analysis_query(sql_file_name: str) -> pd.DataFrame:

    if not sql_file_name.endswith('.sql'):
        sql_file_name = sql_file_name + '.sql'
    
    sql_path = SQL_FOLDER / sql_file_name
    
    if not sql_path.exists():
        for f in SQL_FOLDER.glob("*.sql"):
            print("   ", f.name)
        raise FileNotFoundError(f"SQL not found {sql_path}")
    
    conn = sqlite3.connect(DB_PATH)
    with open(sql_path, "r", encoding="utf-8") as file:
        query = file.read()
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    return df