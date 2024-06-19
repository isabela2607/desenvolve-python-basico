import random
def imprime_enforcado(erros):
    with open("gabarito_forca.txt", 'r') as file:
        estagios = file.read().split('---')
    print(estagios[erros])
with open("gabarito_forca.txt", 'r') as file:
    palavras = file.read().splitlines()
palavra_secreta = random.choice(palavras)

erros = 0
acertos = ['_'] * len(palavra_secreta)
tentativas = set()

while erros < 6 and '_' in acertos:
    print(' '.join(acertos))
    letra = input("Digite uma letra: ").lower()
    
    if letra in tentativas:
        print("Você já tentou essa letra.")
        continue

    tentativas.add(letra)
    
    if letra in palavra_secreta:
        for i, char in enumerate(palavra_secreta):
            if char == letra:
                acertos[i] = letra
    else:
        erros += 1
        imprime_enforcado(erros)

if '_' not in acertos:
    print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
else:
    imprime_enforcado(erros)
    print(f"Você perdeu! A palavra era: {palavra_secreta}")
