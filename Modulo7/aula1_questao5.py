frase = input("Digite uma frase: ")
vogais = 'aeiouAEIOU'
indices_vogais = [i for i, char in enumerate(frase) if char in vogais]
print(f"{len(indices_vogais)} vogais")
print(f"Índices {indices_vogais}")
