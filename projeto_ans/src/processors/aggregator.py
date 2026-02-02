import pandas as pd


def agregar_despesas(df: pd.DataFrame) -> pd.DataFrame:
    agrupado = (
        df.groupby(["razao_social", "UF"])
        .agg(
            total_despesas=("valor", "sum"),
            media_trimestral=("valor", "mean"),
            desvio_padrao=("valor", "std"),
        )
        .reset_index()
        .sort_values("total_despesas", ascending=False)
    )

    return agrupado
