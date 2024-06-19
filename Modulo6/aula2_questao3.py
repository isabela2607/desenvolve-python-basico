import random
from collections import Counter
def main():
    lista1 = [random.randint(0, 50) for _ in range(20)]
    lista2 = [random.randint(0, 50) for _ in range(20)]
    interseccao = list(set(lista1) & set(lista2))
    interseccao.sort()  
    contagem_lista1 = Counter(lista1)
    contagem_lista2 = Counter(lista2)
    print(f"lista1 - {lista1}")
    print(f"lista2 - {lista2}")
    print(f"Interseccao - {interseccao}")
    print("Contagem")
    for elemento in interseccao:
        count_lista1 = contagem_lista1.get(elemento, 0)
        count_lista2 = contagem_lista2.get(elemento, 0)
        print(f"{elemento}: (lista1={count_lista1}, lista2={count_lista2})")
main()
