# Automação Anki (Python)

Scripts em Python para **extrair** pares de frases (inglês / português) a partir de páginas configuradas e **criar notas no AnkiWeb** via Selenium.

## O que há nesta pasta

| Ficheiro | Função |
|----------|--------|
| `extract_frases_from_site.py` | Faz pedidos HTTP, analisa HTML e gera `anki_data.csv`. |
| `anki_fill.py` | Abre o Chrome, inicia sessão no AnkiWeb e adiciona cartões a partir do CSV. |
| `urls.txt` | Lista de URLs (uma por linha; linhas com `#` são ignoradas). Usado por defeito pelo extrator. |
| `anki_data.csv` | Saída do extrator e entrada do `anki_fill.py` (gerado ou editado por ti). |
| `requirements.txt` | Dependências Python. |

## Requisitos

- Python 3.10+ recomendado.
- **Chrome** instalado (o Selenium 4 usa na maior parte dos casos o *Chrome for Testing* / gestão automática do *driver*).
- Ligação à Internet para extrair páginas e usar o AnkiWeb.

## Ambiente virtual

Na pasta `anki_python`:

```bash
python3 -m venv .myenv
source .myenv/bin/activate
pip install -r requirements.txt
```

Instala, entre outras: `selenium`, `pandas`, `requests`, `beautifulsoup4`, `tqdm`.

Para sair do ambiente: `deactivate`.

## 1. Extrair frases para o CSV

Com `urls.txt` no diretório atual (comportamento por defeito):

```bash
python extract_frases_from_site.py
```

Saída predefinida: `anki_data.csv`. Ver todas as opções:

```bash
python extract_frases_from_site.py --help
```

Exemplos úteis:

```bash
python extract_frases_from_site.py -u minhas_urls.txt -o saida.csv
python extract_frases_from_site.py --continuar --verbose
python extract_frases_from_site.py --delay 2
```

Ficheiros auxiliares: `progresso.json` (se usares `--continuar`), `extraction.log`.

## 2. Preencher o AnkiWeb

1. Edita `anki_fill.py` e coloca o **email** e a **palavra-passe** da tua conta AnkiWeb (ou extrai isso para variáveis de ambiente numa versão futura do script).
2. No AnkiWeb, escolhe o baralho correto **antes** de correr o script (o fluxo atual abre **Add** após o login).
3. Garante que o ficheiro `anki_data.csv` está na mesma pasta que o script.

```bash
python anki_fill.py
```

O script usa **Chrome** em janela maximizada; não minimizes a janela durante a execução se possível.

## Formato do CSV para o `anki_fill.py`

O ficheiro deve usar **ponto e vírgula** (`;`) como separador e **obrigatoriamente** esta linha de cabeçalho:

```text
Inglês;Português
```

Exemplo:

```text
Inglês;Português
Action movies are a dime a dozen these days.;Filmes de ação se encontram em cada esquina hoje em dia.
```

Isto corresponde ao formato gerado por `extract_frases_from_site.py`.

### Ficheiros só com `frente;verso` (sem cabeçalho)

No repositório, `AnkiV2/Resources/AnkiFrases.csv` está em estilo `inglês;português` **sem** linha de cabeçalho. Para usar com `anki_fill.py`, acrescenta a primeira linha `Inglês;Português` (ou converte o CSV) para coincidir com o que o script espera.

## Segurança

Evita commitar credenciais. Se já expuseste palavras-passe em repositórios ou chats, **altera a palavra-passe** no AnkiWeb e usa ficheiros ignorados pelo Git (por exemplo via `.gitignore`) para dados sensíveis.

## Resolução de problemas

- **`ModuleNotFoundError` (ex.: `bs4`)**: activa o `.myenv` e corre `pip install -r requirements.txt`.
- **`pip install requirements.txt` falha**: o correcto é `pip install -r requirements.txt`.
- **Botão Add cinzento / clique bloqueado**: o script espera o botão ficar clicável; atrasos na rede ou mudanças no AnkiWeb podem exigir ajustar tempos ou XPaths em `anki_fill.py`.
