# Explorando IA Generativa em um Pipeline de ETL com Python

Nesse desafio, um pipeline de ETL foi desenvolvido em Python. O objetivo é criar slogans para filmes usando o Chat-GPT.

Por meio do arquivo [`movies-ids.csv`](movies-ids.csv), obtemos os IDs de alguns 
filmes, e fazemos a __extração__ dos dados desses filmes por meio da API do 
The Movie Database (TMDB) .

Após a extração dos dados, geramos um slogan por meio do Chat-GPT, e fazemos
a __trasnformação__ com esse novo dado. 

Por fim, fazemos o __carregamento__ desses dados em um arquivo local, chamado
`movie-slogans.json`.

## Como Rodar

É possível criar um ambiente virtual para rodar esse projeto a partir do 
comando:

```bash
python3 -m venv .venv
```

Após isso, podemos ativar o ambiente virtual, com o comando:

```bash
source .venv/Scripts/Activate  # Windows
source .venv/bin/activate      # Unix
```

Com o ambiente ativado, podemos baixar os pacotes necessários para o programa
executar com o pip, usando o comando:

```bash
pip install -r requirements.txt
```

Antes de executar o programa, edite o arquivo [`.env.sample`](.env.sample), o renomeando para `.env` e adicionado as chaves para as APIs do
TMDB e da Open Ai. 

Com o ambiente configurado e dependências instaladas, podemos rodar o projeto
com `python3 etl.py`.
