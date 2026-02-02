-- Projeto: Análise de Despesas ANS
-- Banco: PostgreSQL >= 10
-- Autor: KaynanlDev


SET client_encoding = 'UTF8';

-- TABELA: OPERADORAS

CREATE TABLE IF NOT EXISTS operadoras (
    cnpj          CHAR(14) PRIMARY KEY,
    registro_ans  VARCHAR(20),
    razao_social  TEXT,
    modalidade    TEXT,
    uf            CHAR(2)
);


-- TABELA: DESPESAS CONSOLIDADAS

CREATE TABLE IF NOT EXISTS despesas_consolidadas (
    id              BIGSERIAL PRIMARY KEY,
    cnpj            CHAR(14),
    ano             INT NOT NULL,
    trimestre       VARCHAR(2) NOT NULL,
    descricao       TEXT,
    valor_despesa   DECIMAL(15,2),
    data_referencia DATE,
    FOREIGN KEY (cnpj) REFERENCES operadoras(cnpj)
);


-- TABELA: DESPESAS AGREGADAS

CREATE TABLE IF NOT EXISTS despesas_agregadas (
    cnpj           CHAR(14),
    ano            INT,
    trimestre      VARCHAR(2),
    total_despesas DECIMAL(15,2)
);


CREATE INDEX IF NOT EXISTS idx_despesas_cnpj
ON despesas_consolidadas(cnpj);

CREATE INDEX IF NOT EXISTS idx_despesas_ano_trimestre
ON despesas_consolidadas(ano, trimestre);

CREATE INDEX IF NOT EXISTS idx_operadoras_uf
ON operadoras(uf);

COPY despesas_consolidadas (
    cnpj,
    ano,
    trimestre,
    descricao,
    valor_despesa,
    data_referencia
)
FROM 'C:/Users/kayna/Documents/teste-estagio/projeto_ans/output/consolidado.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';


COPY despesas_agregadas (
    cnpj,
    ano,
    trimestre,
    total_despesas
)
FROM 'C:/Users/kayna/Documents/teste-estagio/projeto_ans/data/output/despesas_agregadas.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8';