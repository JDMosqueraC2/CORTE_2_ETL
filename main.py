from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader
from EDA.analyzer import Analyzer

def main():
    # Rutas
    input_path = "data/raw/stock_senti_analysis.csv"
    output_path = "data/processed/clean_stock_senti_analysis.csv"

    # 1 EXTRAER
    extractor = Extractor(input_path)
    df = extractor.extract()

    # 2️ TRANSFORMAR / LIMPIAR
    transformer = Transformer(df)
    clean_df = transformer.clean()

    # 3️ CARGAR
    loader = Loader(output_path)
    loader.load(clean_df)

    # 4️ ANÁLISIS EXPLORATORIO (EDA)
    analyzer = Analyzer(clean_df)
    analyzer.run_eda()

    print("\n ETL completado exitosamente ")

if __name__ == "__main__":
    main()
