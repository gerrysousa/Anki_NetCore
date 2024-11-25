# Anki_NetCore
Projeto de automação para adicionar frases ao Anki Web em python

Esse projeto é uma automação para facilitar a inserção de frases no Anki Web.

Obs.:
No diretório "AnkiV2/Resources/" existe um arquivo "AnkiFrases.csv" com as frases que serão lidas pela automação e inseridas no Anki Web.

A estrutura do CSV é: 

```
front;back
front;back
front;back
front;back
```

Onde "front" é a frase que se deseja aprender e "back" é o significado/tradução da primeira frase;
Ex.:
```
She said that to you?;Ela falou isso para você? 
```


Crie um ambiente virtual:

```bash
python3 -m venv myenv
```
Ative o ambiente virtual:

```bash
source myenv/bin/activate
```

Instale o Selenium no ambiente virtual:

```bash
pip install selenium pandas
```
Use o Python do ambiente virtual para executar seu script.

```bash
python anki_fill.py
```
Para sair do ambiente virtual:

```bash
deactivate
```



