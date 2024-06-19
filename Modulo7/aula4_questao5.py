import csv

livros = [
    {"Título": "O Senhor dos Anéis", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 1178},
    {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
    {"Título": "O Apanhador no Campo de Centeio", "Autor": "J.D. Salinger", "Ano de publicação": 1951, "Número de páginas": 277},
]

with open("meus_livros.csv", 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Título", "Autor", "Ano de publicação", "Número de páginas"])
    writer.writeheader()
    for livro in livros:
        writer.writerow(livro)

print("Arquivo 'meus_livros.csv' criado com sucesso.")
