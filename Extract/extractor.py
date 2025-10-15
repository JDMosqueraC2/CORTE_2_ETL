import pandas as pd
import os

class Extractor:
    def __init__(self, input_path):
        self.input_path = input_path

    def extract(self):
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        
        # Intentar leer con codificación alternativa
        try:
            df = pd.read_csv(self.input_path, encoding="utf-8", low_memory=False)
        except UnicodeDecodeError:
            df = pd.read_csv(self.input_path, encoding="latin1", low_memory=False)
        
        print(f" Archivo cargado correctamente: {self.input_path}")
        return df
