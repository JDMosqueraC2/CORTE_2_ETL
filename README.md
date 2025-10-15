# CORTE_2_ETL
# ETL - Stock Sentiment Analysis

Proyecto ETL que:
- Extrae `data/raw/stock_senti_analysis.csv`
- Transforma/limpia datos (fechas, duplicados, nulos, tipos, normalizaciones)
- Carga dataset limpio en CSV, Parquet y SQLite (`data/processed/`)
- Genera 5 gráficas EDA en `reports/figures/`

## Estructura
(..lista de carpetas..)

## Requisitos
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
