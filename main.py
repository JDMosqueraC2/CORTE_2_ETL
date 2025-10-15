from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader
from EDA.eda import run_all_eda
import pandas as pd
import os

def main():
    # 1. Extraer
    extractor = Extractor(Config.RAW_CSV)
    df = extractor.extract()

    # 2. Transformar
    transformer = Transformer(df)
    df_clean = transformer.transform(Config)

    # 3. Mantener solo las columnas solicitadas (ej. name, colors, rarity)
    # COMO PEDISTE: solo name, colors, rarity -> verificamos si existen
    keep = ["name", "colors", "rarity"]
    existing_keep = [c for c in keep if c in df_clean.columns]
    df_clean = df_clean[existing_keep].copy()
    print(f"[Main] Columnas finales conservadas: {existing_keep}")

    # 4. Cargar: CSV, Parquet y SQLite
    loader = Loader(df_clean)
    loader.save_csv(Config.PROCESSED_CSV)
    loader.save_parquet(Config.PROCESSED_PARQUET)
    loader.save_sqlite(Config.SQLITE_DB, table_name="stock_senti")

    # 5. EDA: se ejecuta sobre el df limpio (si hay columnas relevantes)
    run_all_eda(df_clean, Config)

if __name__ == "__main__":
    main()
