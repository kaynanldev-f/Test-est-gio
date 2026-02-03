from fastapi import APIRouter
from app.database import get_connection

router = APIRouter(prefix="/api/estatisticas", tags=["Estatísticas"])


@router.get("")
def estatisticas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Total e média
    cursor.execute(
        """
        SELECT
            SUM(total_despesas) AS total,
            AVG(total_despesas) AS media
        FROM despesas_agregadas
        """
    )
    resumo = cursor.fetchone()

    # Top 5 operadoras
    cursor.execute(
        """
        SELECT o.razao_social, SUM(d.total_despesas) AS total
        FROM despesas_agregadas d
        JOIN operadoras o ON o.cnpj = d.cnpj
        GROUP BY o.razao_social
        ORDER BY total DESC
        LIMIT 5
        """
    )
    top5 = cursor.fetchall()

    cursor.close()
    conn.close()

    return {
        "total_despesas": resumo["total"],
        "media_despesas": resumo["media"],
        "top_5_operadoras": top5,
    }