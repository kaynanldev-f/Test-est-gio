from pydantic import BaseModel
from typing import List


class Operadora(BaseModel):
    cnpj: str
    razao_social: str
    uf: str
    modalidade: str


class OperadoraDetalhe(Operadora):
    pass


class Despesa(BaseModel):
    ano: int
    trimestre: str
    total_despesas: float


class PaginatedResponse(BaseModel):
    data: List
    page: int
    limit: int
    total: int