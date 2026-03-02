from db import run_create_tables
from extract import extract_from_csv
from transform import transform_sales
from load import load_to_sqlite

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DB_PATH = "data/database/sales.db"
CREATE_SQL = "sql/create_tables.sql"
DATA_PATH = "data/raw/supermarketanalysis.csv"


def main():
    try:
        logger.info("Starting pipeline")

        run_create_tables(DB_PATH, CREATE_SQL)
        logger.info("Tables created.")

        df_raw = extract_from_csv(DATA_PATH)
        logger.info(f"Raw data extracted: {len(df_raw)} lines")

        df_clean = transform_sales(df_raw)
        logger.info(f"clean data: {len(df_clean)} lines")

        load_to_sqlite(df_clean, DB_PATH)

        logger.info("Pipeline executed")

    except Exception as e:
        logger.error(f"Erro during execution: {type(e).__name__}: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()