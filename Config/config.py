class Config:
    # Rutas de entrada / salida
    RAW_CSV = "data/raw/stock_senti_analysis.csv"
    PROCESSED_CSV = "data/processed/stock_senti_clean.csv"
    PROCESSED_PARQUET = "data/processed/stock_senti_clean.parquet"
    SQLITE_DB = "data/processed/stock_senti.db"

    # EDA output
    FIGURES_DIR = "reports/figures"

    # Opciones
    DATE_COLS = ["date", "Date", "datetime"]  # intentamos detectar
