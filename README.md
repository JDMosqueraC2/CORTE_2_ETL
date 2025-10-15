# CORTE_2_ETL
# ETL - Stock Sentiment Analysis

Proyecto ETL que:
- Extrae `data/raw/stock_senti_analysis.csv`
- Transforma/limpia datos (fechas, duplicados, nulos, tipos, normalizaciones)
- Carga dataset limpio en CSV, Parquet y SQLite (`data/processed/`)
- Genera 5 gráficas EDA en `reports/figures/`

## Estructura
│
├── main.py # Orquestador del proceso ETL completo
│
├── Extract/
│ └── extractor.py # Extrae los datos desde el archivo CSV
│
├── Transform/
│ └── transformer.py # Limpieza y normalización de los datos
│
├── Load/
│ └── loader.py # Guarda el dataset limpio
│
├── EDA/
│ └── analyzer.py # Análisis exploratorio y generación de gráficas
│
└── data/
├── raw/ # Dataset original
│ └── stock_senti_analysis.csv
├── processed/ # Dataset limpio
└── plots/ # Gráficas generadas (EDA)

---

## ⚙️ Tecnologías utilizadas

- 🐍 **Python 3.12+**
- 📦 **pandas** — manejo y limpieza de datos  
- 📊 **matplotlib** — generación de gráficas  
- 💾 **os** — manejo de rutas y archivos  
- 🧱 **Git** y **GitHub** — control de versiones  
- (Opcional) **SQLite3 / Parquet** — almacenamiento estructurado  


## Requisitos
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
