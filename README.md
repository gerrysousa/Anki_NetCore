# Anki_NetCore
Projeto de automação para adicionar frases ao Anki Web


Esse projeto é uma automação para facilitar a inserção de frases no Anki Web.

Obs.:
No diretório "AnkiV2/Resources/" existe um arquivo "AnkiFrases.csv" com as frases que serão lidas pela automação e inseridas no Anki Web.

A estrutura do CSV é: 
front;back

Onde "front" é a frase que se deseja aprender e "back" é o significado/tradução da primeira frase;

Para executar a automação, basta inserir as frases no arquivo CSV, abrir o projeto no Visual Studio e executar o teste "InserirNovasFrasesTeste".
ou executar os comandos 

$ dotnet restore
$ dotnet build C:\workspace\Anki_NetCore\AnkiV2.csproj
$ dotnet test C:\workspace\Anki_NetCore\AnkiV2\bin\Debug\netcoreapp3.1\AnkiV2.dll
