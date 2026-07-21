#!/usr/bin/env python3
"""Busca URLs de categorias do Mairo Vergara via RSS e gera arquivos de lista."""

import argparse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

CATEGORIAS = {
    "o-que-significa": {
        "nome": "O que significa em inglês?",
        "feed": "https://www.mairovergara.com/category/o-que-significa-em-ingles/feed/",
        "filtro_slug": None,
    },
    "como-se-diz": {
        "nome": "Como se diz em inglês?",
        "feed": "https://www.mairovergara.com/category/como-se-diz-em-ingles/feed/",
        "filtro_slug": "como-se-diz-",
    },
}


def carregar_urls_de_arquivo(arquivo):
    """Carrega URLs de um arquivo texto, ignorando comentários e linhas vazias."""
    path = Path(arquivo)
    if not path.exists():
        return set()
    urls = set()
    with path.open(encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha and not linha.startswith("#"):
                urls.add(linha)
    return urls


def buscar_artigos_categoria(feed_url, data_min=None, data_max=None, filtro_slug=None):
    """Percorre o feed RSS paginado e retorna (data, url) dentro do intervalo."""
    artigos = []
    pagina = 1
    parar = False

    while not parar:
        url = feed_url if pagina == 1 else f"{feed_url}?paged={pagina}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
        except Exception as exc:
            raise RuntimeError(f"Erro ao buscar página {pagina} do feed: {exc}") from exc

        root = ET.fromstring(data)
        itens = root.find("channel").findall("item")
        if not itens:
            break

        pagina_artigos = []
        for item in itens:
            link = item.find("link").text.strip()
            pub_dt = parsedate_to_datetime(item.find("pubDate").text.strip())
            if pub_dt.tzinfo is None:
                pub_dt = pub_dt.replace(tzinfo=timezone.utc)
            pagina_artigos.append((pub_dt, link))

        for pub_dt, link in pagina_artigos:
            if filtro_slug and filtro_slug not in link:
                continue
            if data_max and pub_dt > data_max:
                continue
            if data_min and pub_dt < data_min:
                parar = True
                break
            artigos.append((pub_dt, link))

        mais_antigo = min(dt for dt, _ in pagina_artigos)
        if parar or (data_min and mais_antigo < data_min):
            break
        pagina += 1

    artigos.sort(key=lambda x: x[0], reverse=True)
    return artigos


def parse_data(valor):
    if not valor:
        return None
    dt = datetime.strptime(valor, "%Y-%m-%d")
    return dt.replace(tzinfo=timezone.utc)


def escrever_arquivo_urls(caminho, urls, cabecalho_extra=None):
    """Grava URLs em arquivo texto no formato usado pelo extrator."""
    linhas = [
        "# Lista de URLs para extração de frases",
        "# Linhas que começam com # são comentários",
    ]
    if cabecalho_extra:
        linhas.extend(cabecalho_extra)
    linhas.append("")

    with Path(caminho).open("w", encoding="utf-8") as f:
        f.write("\n".join(linhas))
        for url in urls:
            f.write(f"{url}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Atualiza listas de URLs a partir de categorias do Mairo Vergara.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python atualizar_urls.py -c o-que-significa -o urls_novas.txt
  python atualizar_urls.py -c o-que-significa --desde 2024-01-24 --excluir urls.txt -o urls_somente_novas.txt
  python atualizar_urls.py -c o-que-significa --mesclar urls.txt
  python atualizar_urls.py -c como-se-diz -o urls_como_se_diz.txt
        """,
    )
    parser.add_argument(
        "-c",
        "--categoria",
        choices=sorted(CATEGORIAS),
        required=True,
        help="Categoria do site a buscar",
    )
    parser.add_argument(
        "-o",
        "--saida",
        help="Arquivo de saída (obrigatório se não usar --mesclar)",
    )
    parser.add_argument(
        "--desde",
        help="Data mínima inclusive (AAAA-MM-DD). Padrão: sem limite inferior",
    )
    parser.add_argument(
        "--ate",
        help="Data máxima inclusive (AAAA-MM-DD). Padrão: hoje",
    )
    parser.add_argument(
        "--excluir",
        action="append",
        default=[],
        metavar="ARQUIVO",
        help="Ignora URLs já presentes neste arquivo (pode repetir)",
    )
    parser.add_argument(
        "--mesclar",
        metavar="ARQUIVO",
        help="Adiciona URLs novas ao topo deste arquivo, sem duplicar",
    )
    parser.add_argument(
        "--sem-filtro-slug",
        action="store_true",
        help="Inclui todos os posts do feed, mesmo fora do padrão de slug da categoria",
    )
    args = parser.parse_args()

    if not args.saida and not args.mesclar:
        parser.error("Informe --saida ou --mesclar")

    categoria = CATEGORIAS[args.categoria]
    data_min = parse_data(args.desde)
    data_max = parse_data(args.ate) or datetime.now(timezone.utc).replace(
        hour=23, minute=59, second=59
    )
    if data_max and not args.ate:
        pass
    elif args.ate:
        data_max = data_max.replace(hour=23, minute=59, second=59)

    filtro_slug = None if args.sem_filtro_slug else categoria["filtro_slug"]
    artigos = buscar_artigos_categoria(
        categoria["feed"],
        data_min=data_min,
        data_max=data_max,
        filtro_slug=filtro_slug,
    )

    urls_excluir = set()
    for arquivo in args.excluir:
        urls_excluir.update(carregar_urls_de_arquivo(arquivo))

    urls = [link for _, link in artigos if link not in urls_excluir]

    if args.mesclar:
        existentes = carregar_urls_de_arquivo(args.mesclar)
        novas = [url for url in urls if url not in existentes]
        ordem_existentes = []
        with Path(args.mesclar).open(encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha and not linha.startswith("#"):
                    ordem_existentes.append(linha)
        urls_finais = novas + [u for u in ordem_existentes if u not in set(novas)]

        cabecalho = [
            f"# Categoria: {categoria['nome']}",
            f"# Atualizado em: {datetime.now().strftime('%d/%m/%Y')}",
            f"# Total: {len(urls_finais)} URLs ({len(novas)} novas adicionadas)",
        ]
        escrever_arquivo_urls(args.mesclar, urls_finais, cabecalho)
        print(f"Mesclado em: {args.mesclar}")
        print(f"  Novas adicionadas: {len(novas)}")
        print(f"  Total no arquivo: {len(urls_finais)}")

    if args.saida:
        cabecalho = [
            f"# Categoria: {categoria['nome']}",
        ]
        if artigos:
            cabecalho.append(
                f"# Período: {artigos[-1][0].strftime('%d/%m/%Y')} a "
                f"{artigos[0][0].strftime('%d/%m/%Y')} ({len(urls)} URLs)"
            )
        if urls_excluir:
            cabecalho.append(f"# Excluídas por duplicata: {len(artigos) - len(urls)}")
        escrever_arquivo_urls(args.saida, urls, cabecalho)
        print(f"Arquivo gerado: {args.saida}")
        print(f"  URLs: {len(urls)}")
        if artigos:
            print(f"  Mais recente: {artigos[0][0].strftime('%d/%m/%Y')}")
            print(f"  Mais antiga:  {artigos[-1][0].strftime('%d/%m/%Y')}")


if __name__ == "__main__":
    main()
