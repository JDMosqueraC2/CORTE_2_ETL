import os
import matplotlib.pyplot as plt
import pandas as pd

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def plot_time_series(df, date_col, value_col, outpath):
    ensure_dir(os.path.dirname(outpath))
    if date_col not in df.columns or value_col not in df.columns:
        print(f"[EDA] No se puede graficar time series: columnas faltan ({date_col}, {value_col})")
        return
    s = df.set_index(date_col).sort_index()[value_col].resample("D").mean()
    plt.figure(figsize=(10,4))
    s.plot()
    plt.title(f"Time series: {value_col}")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()
    print(f"[EDA] Guardada: {outpath}")

def plot_histogram(df, col, outpath, bins=50):
    ensure_dir(os.path.dirname(outpath))
    if col not in df.columns:
        print(f"[EDA] No se puede graficar hist: columna faltante ({col})")
        return
    plt.figure(figsize=(8,4))
    df[col].dropna().plot(kind="hist", bins=bins)
    plt.title(f"Histogram: {col}")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()
    print(f"[EDA] Guardada: {outpath}")

def plot_boxplot_by_category(df, value_col, cat_col, outpath):
    ensure_dir(os.path.dirname(outpath))
    if value_col not in df.columns or cat_col not in df.columns:
        print(f"[EDA] No se puede graficar boxplot: columnas faltan ({value_col},{cat_col})")
        return
    plt.figure(figsize=(10,5))
    df.boxplot(column=value_col, by=cat_col, rot=45)
    plt.suptitle("")
    plt.title(f"{value_col} by {cat_col}")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()
    print(f"[EDA] Guardada: {outpath}")

def plot_top_categories(df, cat_col, agg_col, top_n, outpath):
    ensure_dir(os.path.dirname(outpath))
    if cat_col not in df.columns or agg_col not in df.columns:
        print(f"[EDA] No se puede graficar top categories: columnas faltan ({cat_col},{agg_col})")
        return
    agg = df.groupby(cat_col)[agg_col].mean().sort_values(ascending=False).head(top_n)
    plt.figure(figsize=(8,4))
    agg.plot(kind="bar")
    plt.title(f"Top {top_n} {cat_col} by avg {agg_col}")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()
    print(f"[EDA] Guardada: {outpath}")

def run_all_eda(df, config):
    figs = config.FIGURES_DIR
    # intentamos inferir nombres
    date_col = None
    for c in ["date","datetime","timestamp","ts","publish_date"]:
        if c in df.columns:
            date_col = c
            break

    # 1. time series de sentimiento medio por día (si existe sentiment & date)
    plot_time_series(df, date_col, "sentiment", os.path.join(figs, "sentiment_time_series.png"))

    # 2. histograma de sentiment
    plot_histogram(df, "sentiment", os.path.join(figs, "sentiment_histogram.png"))

    # 3. boxplot de sentiment por ticker (si ticker existe) - se trunca a top 10 tickers
    if "ticker" in df.columns:
        top_tickers = df['ticker'].value_counts().nlargest(10).index.tolist()
        df_top = df[df['ticker'].isin(top_tickers)]
        plot_boxplot_by_category(df_top, "sentiment", "ticker", os.path.join(figs, "sentiment_box_by_ticker.png"))

    # 4. top tickers por sentimiento medio
    plot_top_categories(df, "ticker", "sentiment", 10, os.path.join(figs, "top_tickers_by_sentiment.png"))

    # 5. histograma / distribución de volumen si existe
    plot_histogram(df, "volume", os.path.join(figs, "volume_histogram.png"))

    print("[EDA] Generación de figuras completada.")
