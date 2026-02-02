import pandas as pd


def enriquecer_com_operadoras(df: pd.DataFrame, cadastro: pd.DataFrame) -> pd.DataFrame:
    """
    Estratégia:
    - LEFT JOIN (não perde dados financeiros)
    - Normaliza CNPJ para garantir o merge
    - Remove duplicidades no cadastro
    """

    # normaliza colunas
    df = df.copy()
    cadastro = cadastro.copy()

    # garante string e remove máscara do CNPJ
    df["cnpj"] = df["cnpj"].astype(str).str.replace(r"\D", "", regex=True)
    cadastro["CNPJ"] = cadastro["CNPJ"].astype(str).str.replace(r"\D", "", regex=True)

    cadastro = cadastro.drop_duplicates(subset=["CNPJ"])

    df = df.merge(
        cadastro[["CNPJ", "Data_Registro_ANS", "Razao_Social", "Modalidade", "UF"]],
        left_on="cnpj",
        right_on="CNPJ",
        how="left",
    )

    df.rename(columns={"Razao_Social": "razao_social"}, inplace=True)
    df.drop(columns=["CNPJ"], inplace=True)

    return df
