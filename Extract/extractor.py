import os
import pandas as pd

class Extractor:
    def __init__(self, input_path):
        self.input_path = input_path

    def extract(self):
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")

        # Leemos con low_memory=False para evitar warnings en archivos grandes
        df = pd.read_csv(self.input_path, low_memory=False)
        print(f"[Extractor] Leído {self.input_path} => {df.shape[0]} filas, {df.shape[1]} columnas")
        return df
