from pathlib import Path

import pandas as pd
from config.settings import (
    BASE_URL_CONTABEIS,
    BASE_URL_OPERADORAS,
    OUTPUT_DIR,
    TRIMESTRES,
)
from processors.aggregator import agregar_despesas
from processors.cleaner import limpar_dados
from processors.normalizer import normalizar
from processors.reader import ler_arquivo
from processors.validator import validar_dados
from services.downloader import baixar_zip, listar_zips_trimestre
from services.enricher import enriquecer_com_operadoras
from services.extractor import extrair_zip
from utils.file_utils import criar_pasta, listar_arquivos


def main():
    todos_dados = []

    raw_dir = Path("data/raw")
    extracted_base_dir = Path("data/extracted")

    criar_pasta(raw_dir)
    criar_pasta(extracted_base_dir)

    # 1. PROCESSAMENTO CONTÁBEIS
    for ano, trimestre in TRIMESTRES:
        print(f"\n📊 Processando {ano} - {trimestre}")

        ano_url = f"{BASE_URL_CONTABEIS}{ano}/"
        extract_path = extracted_base_dir / f"{ano}_{trimestre}"

        criar_pasta(extract_path)

        zips = listar_zips_trimestre(ano_url, ano, trimestre)

        if not zips:
            print(f"⏭️ Pulando {ano} {trimestre} (sem arquivos)")
            continue

        for i, zip_url in enumerate(zips):
            zip_path = raw_dir / f"{ano}_{trimestre}_{i}.zip"
            baixar_zip(zip_url, str(zip_path))
            extrair_zip(zip_path, extract_path)

        for arquivo in listar_arquivos(extract_path):
            df = ler_arquivo(arquivo)
            if df is None or df.empty:
                continue

            df = normalizar(df, ano, trimestre)
            df = limpar_dados(df)
            df = validar_dados(df)

            if not df.empty:
                todos_dados.append(df)

    if not todos_dados:
        raise RuntimeError("⚠️ Nenhum dado válido foi processado.")

    df_consolidado = pd.concat(todos_dados, ignore_index=True)

    # 2. ENRIQUECIMENTO
    print("\n🔗 Enriquecendo com dados cadastrais das operadoras")

    cadastro = pd.read_csv(
        f"{BASE_URL_OPERADORAS}Relatorio_cadop.csv",
        sep=";",
        encoding="latin1",
    )

    df_enriquecido = enriquecer_com_operadoras(df_consolidado, cadastro)

    df_enriquecido = df_enriquecido[
        df_enriquecido["razao_social"].notna()
        & (df_enriquecido["razao_social"].str.strip() != "")
    ]

    # 3. AGREGAÇÃO
    print("\n📈 Agregando despesas")

    df_final = agregar_despesas(df_enriquecido)

    # 4. OUTPUT
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    # CONSOLIDADO 
    consolidado_path = output_dir / "despesas_consolidadas.csv"

    df_enriquecido.to_csv(
    consolidado_path,
    index=False,
    sep=";",
    encoding="utf-8-sig",
    )

    print(f"\n📄 CSV consolidado salvo em: {consolidado_path}")

    saida = output_dir / "despesas_agregadas.csv"
    df_final.to_csv(saida, index=False, sep=";", encoding="utf-8-sig")

    print(f"\n✅ CSV final salvo em: {saida}")


if __name__ == "__main__":
    main()
