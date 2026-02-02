import pandas as pd


def normalizar(df, ano, trimestre):
    df.columns = [c.strip() for c in df.columns]

    # Colunas de valor válidas na ANS
    possiveis_colunas_valor = [
        "VL_SALDO_FINAL",
        "VL_SALDO_INICIAL",
    ]

    possiveis_cnpjs = [
        "cnpj",
        "cnpj_operadora",
        "nr_cnpj",
        "cnpj_da_operadora",
    ]

    coluna_cnpj = None
    for col in possiveis_cnpjs:
        if col in df.columns:
            coluna_cnpj = col
            break

    if coluna_cnpj:
        df = df.rename(columns={coluna_cnpj: "cnpj"})
    else:
        df["cnpj"] = None

    df["ano"] = ano
    df["trimestre"] = trimestre

    coluna_valor = None
    for col in possiveis_colunas_valor:
        if col in df.columns:
            coluna_valor = col
            break

    if coluna_valor is None:
        raise ValueError(
            f"Nenhuma coluna de valor encontrada. Colunas disponíveis: {list(df.columns)}"
        )

    df = df.rename(columns={coluna_valor: "valor"})

    # Converte valor para número
    df["valor"] = (
        df["valor"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )

    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    df["ano"] = ano
    df["trimestre"] = trimestre

    return df
