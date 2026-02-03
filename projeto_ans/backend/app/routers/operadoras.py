from fastapi import APIRouter, Query, HTTPException
from app.database import get_connection

router = APIRouter(tags=["Operadoras"])


@router.get("/")
def listar_operadoras(page: int = 1, limit: int = 10):
    offset = (page - 1) * limit

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM operadoras")
    total = cursor.fetchone()["total"]

    cursor.execute(
        """
        SELECT cnpj, razao_social, uf, modalidade
        FROM operadoras
        LIMIT %s OFFSET %s
        """,
        (limit, offset),
    )

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return {
        "data": data,
        "page": page,
        "limit": limit,
        "total": total,
    }


@router.get("/{cnpj}")
def detalhe_operadora(cnpj: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT cnpj, razao_social, uf, modalidade
        FROM operadoras
        WHERE cnpj = %s
        """,
        (cnpj,),
    )

    operadora = cursor.fetchone()

    cursor.close()
    conn.close()

    if not operadora:
        raise HTTPException(status_code=404, detail="Operadora não encontrada")

    return operadora


@router.get("/{cnpj}/despesas")
def despesas_operadora(cnpj: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT ano, trimestre, total_despesas
        FROM despesas_agregadas
        WHERE cnpj = %s
        ORDER BY ano, trimestre
        """,
        (cnpj,),
    )

    despesas = cursor.fetchall()

    cursor.close()
    conn.close()

    return despesas