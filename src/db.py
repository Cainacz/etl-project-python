import sqlite3
from pathlib import Path


def run_create_tables(db_path: str, sql_path: str) -> None:
    with sqlite3.connect(db_path) as conn:
        with open(sql_path, "r", encoding="utf-8") as f:
            sql_script = f.read()

        conn.executescript(sql_script)

    print("Tables created successfully")