import csv

with open("spotify-2023.csv", 'r', encoding='latin-1') as file:
    reader = csv.DictReader(file)
    musicas = list(reader)

top_musicas = {}
for musica in musicas:
    try:
        ano = int(musica["released_year"])
        if 2012 <= ano <= 2022:
            streams = int(musica["streams"])
            if ano not in top_musicas or streams > top_musicas[ano][3]:
                top_musicas[ano] = [musica["track_name"], musica["artist(s)_name"], ano, streams]
    except ValueError:
        continue

resultado = [top_musicas[ano] for ano in sorted(top_musicas)]

for musica in resultado:
    print(musica)
