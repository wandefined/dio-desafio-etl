import os
import requests
from dotenv import load_dotenv
import pandas as pd
import openai
import json

load_dotenv()

TMDB_API_KEY = os.getenv('TMDB_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

df = pd.read_csv('movies-ids.csv')

movie_ids = df['MovieID']

movies = []

# Extrat
for movie_id in movie_ids:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=pt-BR" + \
          f"&api_key={TMDB_API_KEY}"

    response = requests.get(url)
    movies.append(response.json())


# Transform
def generate_ai_slogan(movie):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "Você é um especialista em markting digital."
        },
        {
            "role": "user",
            "content": f"Crie um slogan para o filme {movie['title']}" + \
                       " (máximo de 50 caracteres)"
        }
    ]
    )
    return completion.choices[0].message.content.strip('\"')



for movie in movies:
    slogan = generate_ai_slogan(movie)
    print(slogan)
    movie['slogan'] = slogan

# Load
with open ('movie-slogans.json', 'w+') as result_file:
    print(json.dumps(movies), file=result_file)
