import random

def remover_intervalo_negativo():
    original = [random.randint(-10, 10) for _ in range(20)]

    print("Original:", original)

    maior_intervalo = []
    atual_intervalo = []
    for num in original:
        if num < 0:
            atual_intervalo.append(num)
        else:
            if len(atual_intervalo) > len(maior_intervalo):
                maior_intervalo = atual_intervalo
            atual_intervalo = []
    if len(atual_intervalo) > len(maior_intervalo):
        maior_intervalo = atual_intervalo

    for num in maior_intervalo:
        original.remove(num)

    print("Editada: ", original)

remover_intervalo_negativo()