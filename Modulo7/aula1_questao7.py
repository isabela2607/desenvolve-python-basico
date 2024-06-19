import random
def encrypt(nomes):
    n = random.randint(1, 10)
    nomes_cript = [''.join(chr(((ord(c) - 33 + n) % 94) + 33) for c in nome) for nome in nomes]
    return nomes_cript, n
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)
print(f"Chave de criptografia: {chave_aleatoria}")
print(f"Nomês criptografados: {nomes_cript}")
