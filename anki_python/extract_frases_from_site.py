import requests
from bs4 import BeautifulSoup
import re
import csv
import argparse
import logging
import time
from pathlib import Path
from tqdm import tqdm
import json
from datetime import datetime

def setup_logging(log_file="extraction.log"):
    """Configura sistema de logging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def carregar_urls_de_arquivo(arquivo_urls):
    """Carrega URLs de um arquivo texto"""
    try:
        with open(arquivo_urls, 'r', encoding='utf-8') as f:
            urls = [linha.strip() for linha in f if linha.strip() and not linha.startswith('#')]
        return urls
    except FileNotFoundError:
        logging.error(f"Arquivo de URLs não encontrado: {arquivo_urls}")
        return []

def salvar_progresso(progresso, arquivo_progresso="progresso.json"):
    """Salva o progresso atual"""
    with open(arquivo_progresso, 'w', encoding='utf-8') as f:
        json.dump(progresso, f, ensure_ascii=False, indent=2)

def carregar_progresso(arquivo_progresso="progresso.json"):
    """Carrega progresso anterior"""
    try:
        with open(arquivo_progresso, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"urls_processadas": [], "frases_extraidas": [], "timestamp": None}

def extrair_frases(urls, args, logger):
    """Função principal melhorada para extrair frases"""
    todas_frases = []
    progresso = carregar_progresso(args.progresso) if args.continuar else {"urls_processadas": [], "frases_extraidas": [], "timestamp": None}
    
    # Filtra URLs já processadas se continuando
    if args.continuar:
        urls_restantes = [url for url in urls if url not in progresso.get("urls_processadas", [])]
        todas_frases.extend(progresso.get("frases_extraidas", []))
        logger.info(f"Continuando processamento. {len(urls_restantes)} URLs restantes de {len(urls)} total.")
    else:
        urls_restantes = urls
        logger.info(f"Iniciando processamento de {len(urls)} URLs")
    
    # Progress bar
    pbar = tqdm(urls_restantes, desc="Processando URLs", unit="url")
    
    for url in pbar:
        pbar.set_description(f"Processando: {url[:50]}...")
        
        try:
            frases_da_url = processar_url_individual(url, args, logger)
            
            if frases_da_url:
                todas_frases.extend(frases_da_url)
                logger.info(f"✅ {len(frases_da_url)//2} pares extraídos de: {url}")
                
                # Salva incrementalmente se solicitado
                if args.salvar_incremental:
                    salvar_frases_csv(todas_frases, args.output, incremental=True)
            else:
                logger.warning(f"⚠️  Nenhuma frase encontrada em: {url}")
            
            # Atualiza progresso
            progresso["urls_processadas"].append(url)
            progresso["frases_extraidas"] = todas_frases
            progresso["timestamp"] = datetime.now().isoformat()
            salvar_progresso(progresso, args.progresso)
            
            # Delay entre requisições para ser respeitoso
            if args.delay:
                time.sleep(args.delay)
                
        except Exception as e:
            logger.error(f"❌ Erro ao processar {url}: {str(e)}")
            if args.parar_em_erro:
                logger.error("Parando execução devido ao erro (--parar-em-erro ativado)")
                break
            continue
    
    pbar.close()
    
    # Salva resultado final
    if todas_frases:
        salvar_frases_csv(todas_frases, args.output)
        logger.info(f"🎉 Processamento concluído! Total: {len(todas_frases)//2} pares de frases")
        logger.info(f"📁 Arquivo salvo: {args.output}")
    
    return todas_frases

def processar_url_individual(url, args, logger):
    """Processa uma URL individual com retry"""
    for tentativa in range(args.retry + 1):
        try:
            if tentativa > 0:
                logger.info(f"Tentativa {tentativa + 1} para {url}")
                time.sleep(2 ** tentativa)  # Backoff exponencial
            
            resposta = requests.get(url, timeout=args.timeout)
            resposta.raise_for_status()
            
            # Análise do conteúdo
            sopa = BeautifulSoup(resposta.text, 'html.parser')
            
            # Localiza a div com as frases (padrão do site Mairo Vergara)
            div_conteudo = sopa.find('div', class_='td-post-content td-pb-padding-side')
            if not div_conteudo:
                # Tenta outros seletores comuns
                div_conteudo = sopa.find('div', class_='post-content') or sopa.find('article') or sopa.find('main')
            
            if div_conteudo:
                return extrair_frases_do_conteudo(div_conteudo, url, args, logger)
            else:
                logger.warning(f"Div de conteúdo não encontrada em: {url}")
                return []

        except requests.RequestException as e:
            if tentativa == args.retry:
                logger.error(f"Falha após {args.retry + 1} tentativas para {url}: {str(e)}")
                return []
            continue
        except Exception as e:
            logger.error(f"Erro inesperado ao processar {url}: {str(e)}")
            return []
    
    return []

def extrair_texto_preservando_espacos(elemento):
    """
    Extrai texto de elemento HTML preservando espaços ao redor de tags de formatação
    """
    # Solução simples e eficaz: usar separator=' ' no get_text()
    texto = elemento.get_text(separator=' ', strip=True)
    
    # Limpa espaços múltiplos
    texto = re.sub(r'\s+', ' ', texto).strip()
    
    return texto

def eh_frase_de_exemplo_valida(texto):
    """
    Verifica se o texto contém realmente uma frase de exemplo bilíngue
    """
    texto_lower = texto.lower()
    
    # 1. Filtros de exclusão - NÃO deve conter explicações
    palavras_explicacao = [
        'significa', 'quer dizer', 'tradução', 'literalmente', 'expressão',
        'usada para', 'refere a', 'refere-se a', 'abreviação', 'casos', 'exemplo',
        'vemos que', 'note que', 'em seguida', 'finalmente', 'primeira', 'segunda',
        'terceira', 'prática', 'comum', 'maior parte', 'maioria', 'pode ser traduzido',
        'definição', 'conceito', 'sentido literal', 'sentido figurado'
    ]
    
    # Se contém muitas palavras de explicação, provavelmente não é exemplo
    if any(palavra in texto_lower for palavra in palavras_explicacao):
        return False
    
    # 2. Deve ter formato de duas frases distintas separadas por ponto
    # Regex mais flexível para caracteres acentuados
    match = re.search(r'([A-Z][^.]{10,})\.\s*([A-ZÀ-ÿ][^.]{10,})', texto)
    if not match:
        return False
    
    frase1 = match.group(1).strip()
    frase2 = match.group(2).strip()
    
    # 3. A primeira frase deve ser claramente em inglês
    palavras_inglesas_frase = ['the', 'a', 'an', 'they', 'we', 'i', 'you', 'he', 'she', 'it', 
                              'have', 'has', 'had', 'will', 'would', 'can', 'could', 'must',
                              'should', 'to', 'and', 'or', 'but', 'with', 'for', 'from']
    
    frase1_lower = frase1.lower()
    palavras_inglesas_encontradas = sum(1 for palavra in palavras_inglesas_frase if f' {palavra} ' in f' {frase1_lower} ')
    
    # Deve ter pelo menos 2 palavras claramente inglesas
    if palavras_inglesas_encontradas < 2:
        return False
    
    # 4. A segunda frase deve ser claramente em português
    palavras_portuguesas_frase = ['de', 'da', 'do', 'em', 'na', 'no', 'para', 'com', 'por',
                                 'que', 'se', 'um', 'uma', 'o', 'a', 'os', 'as', 'ele', 'ela',
                                 'eles', 'elas', 'eu', 'você', 'nós', 'tem', 'têm', 'é', 'são']
    
    frase2_lower = frase2.lower()
    palavras_portuguesas_encontradas = sum(1 for palavra in palavras_portuguesas_frase if f' {palavra} ' in f' {frase2_lower} ')
    
    # Deve ter pelo menos 2 palavras claramente portuguesas
    if palavras_portuguesas_encontradas < 2:
        return False
    
    # 5. Filtro final: primeira frase NÃO deve ser definição em português
    if any(palavra in frase1_lower for palavra in ['significa', 'quer dizer', 'tradução']):
        return False
    
    return True

def extrair_frases_do_conteudo(div_conteudo, url, args, logger):
    """Extrai frases do conteúdo HTML - apenas frases seguidas por figure wp-block-audio"""
    paragrafos = div_conteudo.find_all('p')
    frases_da_url = []
    
    # Procura por parágrafos seguidos por figure com classe wp-block-audio
    for i, paragrafo in enumerate(paragrafos):
        # Verifica se o próximo elemento sibling é uma figure com wp-block-audio
        proximo_elemento = paragrafo.find_next_sibling()
        
        if (proximo_elemento and 
            proximo_elemento.name == 'figure' and 
            'wp-block-audio' in proximo_elemento.get('class', [])):
            
            # Usa a nova função que preserva espaços
            texto = extrair_texto_preservando_espacos(paragrafo)
            
            # Verifica se o texto tem conteúdo válido
            if texto and len(texto) > args.min_length:
                # Verifica se tem padrão de frase bilíngue (inglês + português)
                if tem_padrao_frase_bilingue_simples(texto):
                    frases_da_url.append(texto)
                    
                    if args.verbose:
                        logger.info(f"📢 Encontrou frase com áudio: {texto[:60]}...")
    
    # Processa as frases encontradas
    frases_processadas = []
    for frase_completa in frases_da_url:
        frases_separadas = separar_frases_especificas(frase_completa)
        if frases_separadas and len(frases_separadas) == 2:
            # Validação final mais específica para o formato do site
            if validacao_especifica_mairo_vergara(frases_separadas[0], frases_separadas[1]):
                frases_processadas.extend(frases_separadas)
                
                if args.verbose:
                    logger.info(f"✓ Extraído: {frases_separadas[0][:50]}... | {frases_separadas[1][:30]}...")
    
    return frases_processadas

def eh_explicacao_obvia(texto):
    """
    Elimina APENAS explicações muito óbvias
    """
    texto_lower = texto.lower()
    
    # Só filtra explicações muito claras
    if 'significa, literalmente' in texto_lower:
        return True
    if texto_lower.startswith('dig deep significa'):
        return True
    if 'pode ser traduzido como' in texto_lower:
        return True
    if 'definição de' in texto_lower:
        return True
    
    return False

def tem_padrao_frase_bilingue_simples(texto):
    """
    Verifica padrão simples de frase bilíngue específico para o site
    """
    # Deve ter pelo menos um ponto separando as frases
    if '.' not in texto:
        return False
    
    # Divide o texto em sentenças
    sentencas = [s.strip() for s in texto.split('.') if s.strip()]
    if len(sentencas) < 2:
        return False
    
    # Verifica se tem características de inglês e português
    texto_lower = texto.lower()
    
    # Palavras comuns em inglês
    tem_ingles = any(palavra in texto_lower for palavra in [
        ' the ', ' a ', ' an ', ' this ', ' that ', ' have ', ' has ', ' will ',
        ' they ', ' we ', ' you ', ' he ', ' she ', ' it ', ' is ', ' are '
    ])
    
    # Palavras comuns em português
    tem_portugues = any(palavra in texto_lower for palavra in [
        ' de ', ' da ', ' do ', ' em ', ' na ', ' no ', ' para ', ' com ',
        ' que ', ' um ', ' uma ', ' o ', ' a ', ' ele ', ' ela ', ' tem ', ' é '
    ])
    
    return tem_ingles and tem_portugues

def separar_frases_especificas(texto_completo):
    """
    Separa frases específicas do formato do site Mairo Vergara
    """
    # Remove conteúdo extra e normaliza
    texto_limpo = re.sub(r'\s+', ' ', texto_completo.strip())
    
    # Padrão principal: primeira frase termina com ponto, segunda começa maiúscula
    # Busca por padrão: "Frase em inglês. Frase em português."
    match = re.search(r'^([A-Z][^.]{15,})\.\s*([A-ZÀ-ÿ][^.]{15,})\.?', texto_limpo)
    
    if match:
        frase_inglesa = match.group(1).strip() + '.'
        frase_portuguesa = match.group(2).strip()
        if not frase_portuguesa.endswith('.'):
            frase_portuguesa += '.'
        
        # Limpa espaços extras
        frase_inglesa = re.sub(r'\s+', ' ', frase_inglesa).strip()
        frase_portuguesa = re.sub(r'\s+', ' ', frase_portuguesa).strip()
        
        # Substitui ponto e vírgula por vírgula para evitar problemas no CSV
        frase_inglesa = frase_inglesa.replace(';', ',')
        frase_portuguesa = frase_portuguesa.replace(';', ',')
        
        return [frase_inglesa, frase_portuguesa]
    
    return None

def validacao_especifica_mairo_vergara(frase_inglesa, frase_portuguesa):
    """
    Validação específica para o formato das frases do site Mairo Vergara
    """
    # Comprimentos mínimos
    if len(frase_inglesa) < 20 or len(frase_portuguesa) < 20:
        return False
    
    # Não deve conter palavras de explicação
    palavras_explicacao = ['significa', 'quer dizer', 'expressão', 'tradução']
    texto_combinado = (frase_inglesa + ' ' + frase_portuguesa).lower()
    
    if any(palavra in texto_combinado for palavra in palavras_explicacao):
        return False
    
    # Verifica se realmente tem características das respectivas línguas
    frase_ing_lower = frase_inglesa.lower()
    frase_pt_lower = frase_portuguesa.lower()
    
    # Frase inglesa deve ter palavras típicas do inglês
    palavras_inglesas = ['the', 'a', 'an', 'this', 'that', 'have', 'has', 'will', 'they', 'we', 'he', 'she', 'it']
    tem_ingles = any(f' {palavra} ' in f' {frase_ing_lower} ' for palavra in palavras_inglesas)
    
    # Frase portuguesa deve ter palavras típicas do português
    palavras_portuguesas = ['de', 'da', 'do', 'em', 'na', 'no', 'para', 'com', 'que', 'um', 'uma', 'o', 'a', 'ele', 'ela']
    tem_portugues = any(f' {palavra} ' in f' {frase_pt_lower} ' for palavra in palavras_portuguesas)
    
    return tem_ingles and tem_portugues

def tem_padrao_frase_bilingue(texto):
    """
    Versão mais permissiva - verifica padrão básico
    """
    # Deve ter pelo menos um ponto
    if '.' not in texto:
        return False
    
    # Deve ter pelo menos duas sentenças distintas
    sentencas = re.split(r'\.+', texto)
    if len(sentencas) < 2:
        return False
    
    # Deve ter palavras em inglês E português
    texto_lower = texto.lower()
    
    tem_ingles = any(palavra in texto_lower for palavra in ['the', 'a', 'they', 'we', 'i', 'you', 'he', 'she', 'it', 'have', 'has', 'had', 'to'])
    tem_portugues = any(palavra in texto_lower for palavra in ['de', 'em', 'para', 'com', 'que', 'um', 'uma', 'o', 'a', 'ele', 'ela'])
    
    return tem_ingles and tem_portugues

def validacao_final_permissiva(frase_inglesa, frase_portuguesa):
    """
    Validação final mais permissiva - só elimina casos muito óbvios
    """
    # Elimina frases muito curtas
    if len(frase_inglesa) < 15 or len(frase_portuguesa) < 15:
        return False
    
    # Elimina se tem palavras de explicação nas frases
    palavras_proibidas = ['significa', 'quer dizer', 'tradução', 'expressão usada']
    frase_completa = (frase_inglesa + ' ' + frase_portuguesa).lower()
    
    if any(palavra in frase_completa for palavra in palavras_proibidas):
        return False
    
    return True

def salvar_frases_csv(frases, nome_arquivo="anki_data.csv", incremental=False):
    """
    Salva as frases em formato CSV para importar no Anki
    """
    try:
        # Se incremental, adiciona timestamp ao nome
        if incremental:
            path = Path(nome_arquivo)
            timestamp = datetime.now().strftime("%H%M%S")
            nome_arquivo = path.parent / f"{path.stem}_temp_{timestamp}{path.suffix}"
        
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv, delimiter=';')
            
            # Header do CSV
            escritor.writerow(['Inglês', 'Português'])
            
            # Escreve as frases em pares
            for i in range(0, len(frases), 2):
                if i + 1 < len(frases):
                    escritor.writerow([frases[i], frases[i + 1]])
        
        if not incremental:
            logging.info(f"Frases salvas em: {nome_arquivo}")
            logging.info(f"Total de pares de frases: {len(frases) // 2}")
        
    except Exception as e:
        logging.error(f"Erro ao salvar CSV: {str(e)}")

def criar_arquivo_urls(urls, nome_arquivo="urls.txt"):
    """Cria um arquivo com as URLs para facilitar o gerenciamento"""
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write("# Lista de URLs para extração de frases\n")
        f.write("# Linhas que começam com # são comentários\n\n")
        for url in urls:
            f.write(f"{url}\n")
    logging.info(f"Arquivo de URLs criado: {nome_arquivo}")

def main():
    parser = argparse.ArgumentParser(
        description="Extrator de frases bilíngues de sites de idiomas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python extract_frases_from_site.py                                    # Usa urls.txt se existir
  python extract_frases_from_site.py --urls-arquivo minhas_urls.txt     # Usa arquivo específico
  python extract_frases_from_site.py --continuar --verbose              # Continua processamento
  python extract_frases_from_site.py --delay 2 --retry 3 --output meu_arquivo.csv
        """
    )
    
    # Argumentos de entrada
    parser.add_argument('--urls-arquivo', '-u', 
                       help='Arquivo de texto com URLs (uma por linha). Se não especificado, usa urls.txt por padrão se existir')
    parser.add_argument('--output', '-o', default='anki_data.csv',
                       help='Nome do arquivo CSV de saída (padrão: anki_data.csv)')
    
    # Controle de execução
    parser.add_argument('--continuar', '-c', action='store_true',
                       help='Continua processamento anterior usando arquivo de progresso')
    parser.add_argument('--progresso', default='progresso.json',
                       help='Arquivo para salvar/carregar progresso (padrão: progresso.json)')
    parser.add_argument('--delay', '-d', type=float, default=1.0,
                       help='Delay em segundos entre requisições (padrão: 1.0)')
    parser.add_argument('--timeout', '-t', type=int, default=30,
                       help='Timeout para requisições em segundos (padrão: 30)')
    parser.add_argument('--retry', '-r', type=int, default=2,
                       help='Número de tentativas em caso de erro (padrão: 2)')
    
    # Filtros e configurações
    parser.add_argument('--min-length', '-m', type=int, default=50,
                       help='Comprimento mínimo de texto para considerar (padrão: 50)')
    parser.add_argument('--salvar-incremental', '-i', action='store_true',
                       help='Salva arquivo CSV após cada URL processada')
    
    # Controle de erro e logging
    parser.add_argument('--parar-em-erro', action='store_true',
                       help='Para execução ao encontrar o primeiro erro')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Mostra informações detalhadas durante o processamento')
    parser.add_argument('--log-file', default='extraction.log',
                       help='Arquivo de log (padrão: extraction.log)')
    
    # Utilitários
    parser.add_argument('--criar-urls-arquivo', action='store_true',
                       help='Cria arquivo urls.txt com as URLs hardcoded do script')
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logging(args.log_file)
    
    # Se solicitado, cria arquivo de URLs
    if args.criar_urls_arquivo:
        urls_padrao = [
            "https://www.mairovergara.com/dig-deep-o-que-significa-esta-expressao/",
            "https://www.mairovergara.com/add-insult-to-injury-o-que-significa-esta-expressao/",
            "https://www.mairovergara.com/at-arms-length-o-que-significa-esta-expressao/",
            "https://www.mairovergara.com/have-been-meaning-to-o-que-significa-esta-expressao/",
            "https://www.mairovergara.com/in-my-book-o-que-significa-esta-expressao/",
            "https://www.mairovergara.com/have-a-hunch-o-que-significa-esta-expressao/",
        ]
        criar_arquivo_urls(urls_padrao)
        return
    
    # Carrega URLs
    if args.urls_arquivo:
        # Se especificado explicitamente, usa o arquivo especificado
        urls = carregar_urls_de_arquivo(args.urls_arquivo)
        if not urls:
            logger.error(f"Nenhuma URL encontrada no arquivo: {args.urls_arquivo}")
            return
        logger.info(f"Usando URLs do arquivo especificado: {args.urls_arquivo}")
    else:
        # Tenta usar urls.txt por padrão
        arquivo_padrao = "urls.txt"
        if Path(arquivo_padrao).exists():
            urls = carregar_urls_de_arquivo(arquivo_padrao)
            if urls:
                logger.info(f"Usando URLs do arquivo padrão: {arquivo_padrao} ({len(urls)} URLs encontradas)")
            else:
                logger.warning(f"Arquivo {arquivo_padrao} existe mas não contém URLs válidas")
                urls = []
        else:
            urls = []
        
        # Se não conseguiu carregar do arquivo padrão, usa URLs hardcoded
        if not urls:
            urls = [
                "https://www.mairovergara.com/dig-deep-o-que-significa-esta-expressao/",
                "https://www.mairovergara.com/add-insult-to-injury-o-que-significa-esta-expressao/",
                "https://www.mairovergara.com/at-arms-length-o-que-significa-esta-expressao/",
                "https://www.mairovergara.com/have-been-meaning-to-o-que-significa-esta-expressao/",
                "https://www.mairovergara.com/in-my-book-o-que-significa-esta-expressao/",
                "https://www.mairovergara.com/have-a-hunch-o-que-significa-esta-expressao/",
            ]
            logger.info(f"Usando URLs padrão do script ({len(urls)} URLs)")
    
    # Executa extração
    try:
        frases = extrair_frases(urls, args, logger)
        if frases:
            logger.info(f"✨ Sucesso! {len(frases)//2} pares de frases extraídos")
        else:
            logger.warning("Nenhuma frase foi extraída")
    except KeyboardInterrupt:
        logger.info("⏹️  Processamento interrompido pelo usuário")
        logger.info("Use --continuar para retomar o processamento")
    except Exception as e:
        logger.error(f"Erro durante o processamento: {str(e)}")

def separar_frases(texto_completo):
    """
    Separa frases em inglês das traduções em português
    """
    # Remove conteúdo entre parênteses (explicações extras)
    texto_limpo = re.sub(r'\([^)]*\)', '', texto_completo)
    
    # Correções básicas e específicas
    texto_limpo = re.sub(r'([a-z])([A-Z])', r'\1 \2', texto_limpo)
    texto_limpo = re.sub(r'\s+', ' ', texto_limpo).strip()
    
    # Padrão principal: Frase.Frase em português. (com pontos)
    match = re.search(r'([A-Z][^.]{10,})\.([A-Z\u00C0-\u017F][^.]{10,})', texto_limpo)
    
    if match:
        frase_inglesa = match.group(1).strip() + '.'
        frase_portuguesa = match.group(2).strip()
        if not frase_portuguesa.endswith('.'):
            frase_portuguesa += '.'
        
        # Correções finais simples
        frase_inglesa = corrigir_espacamento(frase_inglesa)
        frase_portuguesa = corrigir_espacamento(frase_portuguesa)
        
        # Substitui ponto e vírgula por vírgula para evitar problemas no CSV
        frase_inglesa = frase_inglesa.replace(';', ',')
        frase_portuguesa = frase_portuguesa.replace(';', ',')
        
        # Validação rigorosa
        if (tem_palavras_inglesas(frase_inglesa) and 
            tem_palavras_portuguesas(frase_portuguesa) and
            eh_frase_exemplo_real(frase_inglesa, frase_portuguesa)):
            return [frase_inglesa, frase_portuguesa]
    
    return None

def eh_frase_exemplo_real(frase_inglesa, frase_portuguesa):
    """
    Validação final para garantir que são frases de exemplo reais
    """
    frase_ing_lower = frase_inglesa.lower()
    frase_pt_lower = frase_portuguesa.lower()
    
    # 1. NÃO deve conter palavras de explicação
    palavras_invalidas = ['significa', 'quer dizer', 'expressão', 'tradução', 'literalmente',
                         'usada para', 'refere a', 'conceito', 'definição']
    
    if any(palavra in frase_ing_lower or palavra in frase_pt_lower for palavra in palavras_invalidas):
        return False
    
    # 2. Frases devem ter comprimento mínimo
    if len(frase_inglesa) < 20 or len(frase_portuguesa) < 20:
        return False
    
    # 3. Frase inglesa deve ter estrutura de frase real (sujeito + verbo)
    palavras_sujeito_ing = ['i', 'you', 'he', 'she', 'it', 'we', 'they', 'this', 'that', 'these', 'those']
    palavras_verbo_ing = ['am', 'is', 'are', 'was', 'were', 'have', 'has', 'had', 'will', 'would', 
                         'can', 'could', 'must', 'should', 'do', 'does', 'did', 'go', 'goes', 'went']
    
    tem_sujeito_ing = any(f' {palavra} ' in f' {frase_ing_lower} ' for palavra in palavras_sujeito_ing)
    tem_verbo_ing = any(f' {palavra} ' in f' {frase_ing_lower} ' for palavra in palavras_verbo_ing)
    
    # 4. Frase portuguesa deve ter estrutura de frase real
    palavras_sujeito_pt = ['eu', 'você', 'ele', 'ela', 'nós', 'eles', 'elas', 'isto', 'isso', 'este', 'esta']
    palavras_verbo_pt = ['sou', 'é', 'são', 'era', 'foram', 'tenho', 'tem', 'têm', 'teve', 'tiveram',
                        'vou', 'vai', 'vão', 'posso', 'pode', 'podem', 'deve', 'devem', 'faço', 'faz']
    
    tem_sujeito_pt = any(f' {palavra} ' in f' {frase_pt_lower} ' for palavra in palavras_sujeito_pt)
    tem_verbo_pt = any(f' {palavra} ' in f' {frase_pt_lower} ' for palavra in palavras_verbo_pt)
    
    # Deve ter pelo menos estrutura básica de frase em uma das duas línguas
    return (tem_sujeito_ing or tem_verbo_ing) and (tem_sujeito_pt or tem_verbo_pt)

def corrigir_espacamento(frase):
    """Corrige problemas comuns de espaçamento"""
    # Correções específicas para termos comuns
    frase = re.sub(r'track\s*record', 'track record', frase, flags=re.IGNORECASE)
    frase = re.sub(r'all\s*I\'?m\s*saying', "all I'm saying", frase, flags=re.IGNORECASE)
    
    # Remove espaços extras antes de pontuação
    frase = re.sub(r'\s+([.!?,:;])', r'\1', frase)
    
    # Padroniza espaços
    frase = re.sub(r'\s+', ' ', frase).strip()
    
    return frase

def tem_palavras_inglesas(texto):
    """Verifica se o texto contém palavras comuns em inglês"""
    palavras_inglesas = ['the', 'a', 'an', 'is', 'are', 'has', 'have', 'with', 'for', 'of', 'in', 'on', 'to', 'and', 'or']
    texto_lower = texto.lower()
    return any(palavra in texto_lower for palavra in palavras_inglesas)

def tem_palavras_portuguesas(texto):
    """Verifica se o texto contém palavras comuns em português"""
    palavras_portuguesas = ['um', 'uma', 'o', 'a', 'os', 'as', 'de', 'da', 'do', 'em', 'na', 'no', 'para', 'com', 'por', 'são', 'é', 'tem', 'têm', 'que', 'se']
    texto_lower = texto.lower()
    return any(palavra in texto_lower for palavra in palavras_portuguesas)

if __name__ == "__main__":
    main()