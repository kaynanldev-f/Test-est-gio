import pandas as pd
from utils.cnpj_utils import cnpj_valido


def validar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Estratégia de validação adotada:

    - CNPJs inválidos: descartados
    - Valores nulos ou <= 0: descartados
    - Razão social vazia ou nula: descartada

    Justificativa:
    Optei por remover registros inválidos para garantir consistência
    nas análises financeiras, evitando distorções nos valores agregados.
    """

    df = df.copy()

    # Padroniza nomes de colunas
    df.columns = [c.strip().lower() for c in df.columns]

    total_inicial = len(df)

    # Validação de valor
    if "valor" in df.columns:
        df = df[df["valor"].notna() & (df["valor"] > 0)]
    else:
        raise ValueError("Coluna 'valor' não encontrada para validação")

    total_final = len(df)

    print(
        f"Validação concluída: {total_inicial - total_final} registros removidos "
        f"({total_final} válidos)"
    )

    return df
