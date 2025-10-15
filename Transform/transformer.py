import pandas as pd

class Transformer:
    def __init__(self, df):
        self.df = df

    def clean(self):
        df = self.df.copy()

        # Eliminar duplicados
        df = df.drop_duplicates()

        # Eliminar filas totalmente vacías
        df = df.dropna(how="all")

        # Rellenar valores nulos con texto o promedio si aplica
        df = df.fillna({
            "Sentiment": "Unknown",
            "Stock": "Unknown"
        })

        # Convertir columnas de fecha si existen
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        print(" Datos limpios correctamente")
        return df
