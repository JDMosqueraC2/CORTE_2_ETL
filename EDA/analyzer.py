import matplotlib.pyplot as plt
import pandas as pd
import os

class Analyzer:
    def __init__(self, df):
        self.df = df

    def run_eda(self):
        os.makedirs("data/plots", exist_ok=True)

        # 1️ Distribución de etiquetas (Label)
        if "Label" in self.df.columns:
            self.df["Label"].value_counts().plot(kind="bar", title="Distribución de etiquetas (Label)")
            plt.xlabel("Etiqueta")
            plt.ylabel("Cantidad")
            plt.tight_layout()
            plt.savefig("data/plots/label_distribution.png")
            plt.close()

        # 2️ Conteo de noticias por fecha
        if "Date" in self.df.columns:
            self.df["Date"] = pd.to_datetime(self.df["Date"], errors="coerce")
            self.df["Date"].value_counts().sort_index().plot(title="Conteo de registros por fecha")
            plt.xlabel("Fecha")
            plt.ylabel("Cantidad de registros")
            plt.tight_layout()
            plt.savefig("data/plots/records_over_time.png")
            plt.close()

        # 3️ Top 10 apariciones de términos en Top1
        if "Top1" in self.df.columns:
            self.df["Top1"].value_counts().head(10).plot(kind="bar", title="Top 10 términos en Top1")
            plt.xlabel("Término")
            plt.ylabel("Frecuencia")
            plt.tight_layout()
            plt.savefig("data/plots/top10_terms.png")
            plt.close()

        # 4️ Comparación de proporciones de etiquetas
        if "Label" in self.df.columns:
            self.df["Label"].value_counts().plot(kind="pie", autopct="%1.1f%%", title="Proporción de etiquetas", ylabel="")
            plt.tight_layout()
            plt.savefig("data/plots/label_pie.png")
            plt.close()

        # 5️ Número promedio de columnas Top no vacías por fila
        top_cols = [c for c in self.df.columns if c.startswith("Top")]
        self.df["non_null_tops"] = self.df[top_cols].notna().sum(axis=1)
        self.df["non_null_tops"].plot(kind="hist", bins=20, title="Distribución del número de Top no vacíos por fila")
        plt.xlabel("Cantidad de valores Top")
        plt.ylabel("Frecuencia")
        plt.tight_layout()
        plt.savefig("data/plots/top_non_null_distribution.png")
        plt.close()

        print(" Gráficas generadas correctamente en data/plots/")
