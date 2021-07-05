# Anki_NetCore
Projeto de automação para adicionar frases ao Anki Web


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

Para executar a automação, basta inserir as frases no arquivo CSV, abrir o projeto no Visual Studio e executar o teste "InserirNovasFrasesTeste".
ou, acessar o diretório do projeto pelo terminal e executar os comandos abaixo: 

```
$ dotnet restore
$ dotnet build C:\workspace\Anki_NetCore\AnkiV2.csproj
$ dotnet test C:\workspace\Anki_NetCore\AnkiV2\bin\Debug\netcoreapp3.1\AnkiV2.dll

```

Para atualizar o chrome faça:
Tente executar os tests: o erro vai dizer qual o versão do chrome instalado na maquina:

`` Mensagem de erro:
   OneTimeSetUp: System.InvalidOperationException : session not created: This version of ChromeDriver only supports Chrome version 87
Current browser version is 91.0.4472.124 with binary path C:\Program Files (x86)\Google\Chrome\Application\chrome.exe (SessionNotCreated)``

Pegue a versão e vai no arquivo "AnkiV2.csproj" e cole no devido lugar "91.0.4472.124"

Execute ````dotnet restore```
E veja se a versão foi atualizada


