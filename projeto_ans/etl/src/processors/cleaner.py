import pandas as pd


def limpar_dados(df):
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    df = df[df["valor"].notna()]
    return df
