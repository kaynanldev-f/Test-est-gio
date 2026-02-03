from fastapi import FastAPI
from app.routers import operadoras, estatisticas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API ANS - Análise de Despesas",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "ok"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    operadoras.router,
    prefix="/api/operadoras",
    tags=["Operadoras"]
)

app.include_router(
    estatisticas.router,
    prefix="/api/estatisticas",
    tags=["Estatísticas"]
)
