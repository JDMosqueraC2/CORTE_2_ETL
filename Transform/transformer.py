import pandas as pd
import os

class Transformer:
    def __init__(self, df):
        self.df = df.copy()

    def normalize_column_names(self):
        # Normalizar nombres: trim + lower + reemplazar espacios por _
        self.df.columns = [c.strip().lower().replace(" ", "_") for c in self.df.columns]

    def detect_date_column(self, candidates):
        for c in candidates:
            c_norm = c.strip().lower()
            if c_norm in self.df.columns:
                return c_norm
        # heurística: buscar columna con 'date' o 'time' en el nombre
        for c in self.df.columns:
            if "date" in c or "time" in c or "ts" in c:
                return c
        return None

    def parse_dates(self, date_col):
        if date_col is None:
            print("[Transformer] No se detectó columna de fecha.")
            return
        try:
            self.df[date_col] = pd.to_datetime(self.df[date_col], errors="coerce")
            # opcional: crear columnas auxiliares
            self.df["year"] = self.df[date_col].dt.year
            self.df["month"] = self.df[date_col].dt.month
            self.df["day"] = self.df[date_col].dt.day
            print(f"[Transformer] Fecha parseada en columna '{date_col}'")
        except Exception as e:
            print("[Transformer] Error parseando fechas:", e)

    def handle_duplicates(self, subset=None):
        before = len(self.df)
        self.df = self.df.drop_duplicates(subset=subset)
        after = len(self.df)
        print(f"[Transformer] Duplicados eliminados: {before - after}")

    def handle_nulls(self, strategy="drop", fill_values=None):
        # strategy: 'drop' | 'fill'
        if strategy == "drop":
            before = len(self.df)
            self.df = self.df.dropna()
            after = len(self.df)
            print(f"[Transformer] Filas con nulos eliminadas: {before - after}")
        elif strategy == "fill":
            if fill_values is None:
                fill_values = {}
            self.df = self.df.fillna(value=fill_values)
            print(f"[Transformer] Nulos rellenados con {fill_values}")

    def normalize_text_columns(self, text_cols):
        for c in text_cols:
            if c in self.df.columns:
                # ejemplo simple: strip y lower
                self.df[c] = self.df[c].astype(str).str.strip()
                # no forzamos lower en nombres (solo limpiar espacios)
        print(f"[Transformer] Normalización básica aplicada a columnas: {text_cols}")

    def cast_types(self, numeric_cols, categorical_cols):
        for c in numeric_cols:
            if c in self.df.columns:
                self.df[c] = pd.to_numeric(self.df[c], errors="coerce")
        for c in categorical_cols:
            if c in self.df.columns:
                self.df[c] = self.df[c].astype("category")
        print(f"[Transformer] Cast types: numeric={numeric_cols}, categorical={categorical_cols}")

    def keep_columns(self, keep):
        existing = [c for c in keep if c in self.df.columns]
        self.df = self.df[existing].copy()
        print(f"[Transformer] Columnas conservadas: {existing}")

    def transform(self, config):
        # pipeline de transformación genérico y seguro (no rompe si faltan columnas)
        self.normalize_column_names()

        # detectar columna de fecha
        date_col = self.detect_date_column(config.DATE_COLS)
        self.parse_dates(date_col)

        # eliminar duplicados (usar columnas clave si existen: ticker + date)
        key_cols = []
        if "ticker" in self.df.columns:
            key_cols.append("ticker")
        if date_col is not None:
            key_cols.append(date_col)
        self.handle_duplicates(subset=key_cols if key_cols else None)

        # manejo de nulos: rellenar campos comunes (si existen)
        fill_values = {}
        if "sentiment" in self.df.columns:
            fill_values["sentiment"] = 0.0
        if "volume" in self.df.columns:
            fill_values["volume"] = 0
        if fill_values:
            self.handle_nulls(strategy="fill", fill_values=fill_values)
        else:
            # si no tenemos fill values, eliminamos filas con nulos
            self.handle_nulls(strategy="drop")

        # normalizaciones
        # normalizamos columnas textuales básicas:
        text_cols = [c for c in ["name", "ticker", "source"] if c in self.df.columns]
        self.normalize_text_columns(text_cols)

        # cast de tipos
        numeric_cols = [c for c in ["sentiment", "close", "open", "volume", "price"] if c in self.df.columns]
        categorical_cols = [c for c in ["rarity", "ticker", "sector"] if c in self.df.columns]
        self.cast_types(numeric_cols, categorical_cols)

        # mantener solo las columnas solicitadas (ejemplo: name, colors, rarity),
        # el caller puede decidir qué columnas mantener. Aquí, no restringimos aún.
        return self.df
