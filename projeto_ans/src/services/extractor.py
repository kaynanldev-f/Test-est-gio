import re
import zipfile
from pathlib import Path


def sanitizar_nome_arquivo(nome: str) -> str:
    # remove path interno do zip
    nome = Path(nome).name

    # remove caracteres de controle
    nome = nome.strip()
    nome = re.sub(r"[\x00-\x1f\x7f]", "", nome)

    return nome


def extrair_zip(zip_path: str | Path, destino: str | Path):
    zip_path = Path(zip_path)
    destino = Path(destino)

    # garante que o diretório de destino existe
    destino.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        for zip_info in zip_ref.infolist():

            # ignora diretórios internos
            if zip_info.is_dir():
                continue

            nome_arquivo = sanitizar_nome_arquivo(zip_info.filename)

            # extrai apenas CSV
            if not nome_arquivo.lower().endswith(".csv"):
                continue

            caminho_destino = destino / nome_arquivo

            with zip_ref.open(zip_info) as origem:
                with open(caminho_destino, "wb") as destino_arquivo:
                    destino_arquivo.write(origem.read())

    print(f"Arquivos extraídos com sucesso em: {destino.resolve()}")
