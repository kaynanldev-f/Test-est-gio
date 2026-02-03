import pandas as pd


def ler_arquivo(caminho):
    if caminho.endswith(".csv") or caminho.endswith(".txt"):
        return pd.read_csv(caminho, sep=None, engine="python")
    elif caminho.endswith(".xlsx"):
        return pd.read_excel(caminho)
    return None
