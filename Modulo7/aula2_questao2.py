def substituir_vogais(frase):
    vogais = "aeiouAEIOU"
    nova_frase = ''.join('*' if char in vogais else char for char in frase)
    return nova_frase

frase = input("Digite uma frase: ")
print(f"Frase modificada: {substituir_vogais(frase)}")
