import os

class Loader:
    def __init__(self, output_path):
        self.output_path = output_path

    def load(self, df):
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        df.to_csv(self.output_path, index=False)
        print(f" Archivo guardado en: {self.output_path}")
