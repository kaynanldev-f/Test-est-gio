from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def criar_sessao():
    session = requests.Session()

    retry = Retry(
        total=5,
        backoff_factor=2,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET"],
    )

    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
            "Connection": "keep-alive",
        }
    )

    return session


def baixar_zip(url: str, destino: str):
    print(f"Baixando ZIP: {url}")

    session = requests.Session()

    retry = Retry(
        total=5,
        backoff_factor=2,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET"],
    )

    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "Connection": "keep-alive",
    }

    with session.get(url, headers=headers, stream=True, timeout=120) as response:
        response.raise_for_status()

        with open(destino, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

    print(f"ZIP salvo em: {destino}")


def listar_links(url):

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for a in soup.find_all("a"):
        href = a.get("href")

        if (
            href
            and str(href).endswith("/")
            and not str(href).startswith("?")
            and href != "../"
        ):
            links.append(href)

    return links


def listar_zips_trimestre(url_ano, ano, trimestre):
    print(f"Acessando URL: {url_ano}")

    session = criar_sessao()

    try:
        response = session.get(url_ano, timeout=60)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Erro ao acessar {url_ano}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    alvo = f"{trimestre}{ano}".lower()
    zips = []

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and str(href).lower().endswith(".zip") and alvo in str(href).lower():
            zips.append(urljoin(url_ano, str(href)))

    if not zips:
        print(f"⚠️ Nenhum ZIP encontrado para {trimestre}{ano}")

    return zips
