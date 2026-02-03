from fastapi import FastAPI
from app.routers import operadoras, estatisticas

app = FastAPI(
    title="API ANS - Análise de Despesas",
    version="1.0.0"
)

app.include_router(operadoras.router, prefix="/operadoras", tags=["Operadoras"])
app.include_router(estatisticas.router, prefix="/estatisticas", tags=["Estatísticas"])