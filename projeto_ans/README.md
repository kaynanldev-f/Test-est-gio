# 📊 Projeto ANS – Demonstrações Contábeis

Este projeto tem como objetivo **automatizar o download, extração, tratamento e consolidação** das demonstrações contábeis disponibilizadas pela **ANS (Agência Nacional de Saúde Suplementar)**, gerando um **CSV final consolidado** pronto para análise.

O projeto foi desenvolvido em **Python**, seguindo uma estrutura modular, com foco em organização, legibilidade e boas práticas — ideal para fins acadêmicos, técnicos e de portfólio.

---

## 🎯 Objetivo

* Acessar os dados públicos da ANS
* Baixar automaticamente os arquivos ZIP por **ano e trimestre**
* Extrair os arquivos CSV
* Padronizar colunas e estruturar os dados
* Limpar valores inválidos
* Consolidar todos os dados em **um único arquivo CSV final**

---

## 🗂️ Estrutura do Projeto

```text
projeto_ans/
│
├── data/
│   ├── raw/            # Arquivos ZIP baixados
│   ├── extracted/      # CSVs extraídos dos ZIPs
│   └── output/         # CSV final consolidado
│
├── src/
│   ├── main.py         # Script principal
│   ├── config/
│   │   └── settings.py # Configurações (anos e trimestres)
│   ├── services/
│   │   ├── downloader.py  # Download dos ZIPs
│   │   └── extractor.py   # Extração dos arquivos
│   ├── processors/
│   │   ├── reader.py      # Leitura dos CSVs
│   │   ├── normalizer.py  # Padronização dos dados
│   │   └── cleaner.py     # Limpeza dos dados
│   └── utils/
│       └── file_utils.py  # Utilidades de arquivos e pastas
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

* **Python 3.10+**
* **Pandas** – manipulação e análise de dados
* **Requests** – download de arquivos
* **Pathlib / OS** – manipulação de arquivos

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/projeto_ans.git
cd projeto_ans
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o script principal

```bash
python src/main.py
```

---

## 📄 Resultado

Ao final da execução, será gerado o arquivo:

```text
data/output/consolidado.csv
```

Esse arquivo contém:

* Dados de todos os trimestres processados
* Coluna `ano`
* Coluna `trimestre`
* Valores normalizados e limpos

Pronto para uso em análises, dashboards ou estudos exploratórios.

---

## 🧹 Tratamento de Dados

Durante o processamento, o projeto:

* Remove espaços extras nos nomes das colunas
* Normaliza nomes de colunas de valor
* Converte valores numéricos inválidos para `NaN`
* Remove registros sem valor válido

---

## 📌 Observações Importantes

* Os dados são públicos e fornecidos pela **ANS**
* Eventuais variações nos nomes das colunas são tratadas automaticamente
* O projeto foi estruturado para facilitar manutenção e evolução

---

## 📈 Possíveis Melhorias Futuras

* Adicionar logs com `logging`
* Criar testes automatizados
* Parametrizar anos e trimestres via CLI
* Exportar para outros formatos (Parquet, SQLite)

---

## 👨‍💻 Autor

Desenvolvido por **Kaynan Teixeira**

⭐ Se este projeto te ajudou de alguma forma, considere dar uma estrela no repositório!
