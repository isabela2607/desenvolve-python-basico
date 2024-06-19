with open("estomago.txt", 'r', encoding='latin-1') as file:
    linhas = file.readlines()

print("Primeiras 25 linhas:")
for linha in linhas[:25]:
    print(linha.strip())

num_linhas = len(linhas)
print(f"\nNúmero de linhas do arquivo: {num_linhas}")

linha_maior = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres: {linha_maior.strip()}")
cont_nonato = sum(linha.lower().count("nonato") for linha in linhas)

cont_iria = sum(linha.lower().count("íria") for linha in linhas)
print(f"\nNúmero de menções ao 'Nonato': {cont_nonato}")
print(f"Número de menções à 'Íria': {cont_iria}")
