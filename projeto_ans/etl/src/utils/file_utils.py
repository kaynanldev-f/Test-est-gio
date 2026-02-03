import os


def criar_pasta(caminho):
    os.makedirs(caminho, exist_ok=True)


def listar_arquivos(pasta):
    arquivos = []
    for raiz, _, files in os.walk(pasta):
        for file in files:
            arquivos.append(os.path.join(raiz, file))
    return arquivos
