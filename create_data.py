import pandas as pd
import requests as req
import json

#Coletando dados de uma playlist

URL = '	https://api.spotify.com/v1/playlists/6FCur4Jei2Lx0Xjs6axzmV/tracks'
TOKEN = ''
#insira seu token

result = req.get(
    URL,
    headers={
        "Authorization": f"Bearer {TOKEN}"
    }
)
result = result.json()

df = pd.DataFrame(result)

#separando informações das músicas

names = []
for i in df['items']:
    names.append(i['track']['name'])  
images = []
for i in df['items']:
    images.append(i['track']['album']['images'][0]['url'])
ids = []
for i in df['items']:
    ids.append(i['track']['id'])

#preparando a url

nome = ids[0]
for i in ids:
    if (i != ids[0]):
        nome = nome +'%2C'+ i
url5 =  'https://api.spotify.com/v1/audio-features?ids=' + nome

#Colentando dados das músicas

response = req.get(
    url5,
    headers={
        "Authorization": f"Bearer {TOKEN}"
    }
)
response = response.json()
dfTracks= pd.DataFrame(response)

#criando dataframe final

dados = pd.DataFrame()
dados['nomes']= names
dados['id']= ids
dados['images']= images


danceability = []
energy = []
loudness=[]
speechiness=[]
instrumentalness=[]
liveness=[]
valence=[]
tempo=[]

for i in dfTracks['audio_features']:
    energy.append(i['energy'])
for i in dfTracks['audio_features']:
    danceability.append(i['danceability'])  
for i in dfTracks['audio_features']:
    loudness.append(i['loudness'])  
for i in dfTracks['audio_features']:
    speechiness.append(i['speechiness'])  
for i in dfTracks['audio_features']:
    instrumentalness.append(i['instrumentalness'])  
for i in dfTracks['audio_features']:
    liveness.append(i['liveness'])  
for i in dfTracks['audio_features']:
    valence.append(i['valence'])  
for i in dfTracks['audio_features']:
    tempo.append(i['tempo']) 

dados['danceability']= danceability
dados['energy']= energy
dados['loudness']= loudness
dados['speechiness']= speechiness
dados['instrumentalness']= instrumentalness
dados['liveness']= liveness
dados['valence']= valence
dados['tempo']= tempo

#inserindo o dataframe em um arquivo csv

dados.to_csv('datamusic', encoding='utf-8', index=False)