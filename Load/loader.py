import os
import sqlite3
import pandas as pd

class Loader:
    def __init__(self, df):
        self.df = df

    def save_csv(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.df.to_csv(path, index=False)
        print(f"[Loader] CSV guardado en: {path}")

    def save_parquet(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.df.to_parquet(path, index=False)
        print(f"[Loader] Parquet guardado en: {path}")

    def save_sqlite(self, db_path, table_name="clean_data"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        conn = sqlite3.connect(db_path)
        self.df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        print(f"[Loader] Guardado en SQLite: {db_path} (tabla: {table_name})")
