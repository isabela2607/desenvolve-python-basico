def main():
    quantidade1 = int(input("Digite a quantidade de elementos da lista 1: "))
    lista1 = []
    for _ in range(quantidade1):
        lista1.append(int(input()))
    quantidade2 = int(input("Digite a quantidade de elementos da lista 2: "))
    lista2 = []
    for _ in range(quantidade2):
        lista2.append(int(input()))
    
    lista_intercalada = []
    i = 0
    j = 0
    while i < quantidade1 and j < quantidade2:
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[j])
        i += 1
        j += 1
    while i < quantidade1:
        lista_intercalada.append(lista1[i])
        i += 1
    while j < quantidade2:
        lista_intercalada.append(lista2[j])
        j += 1
    print("Lista intercalada:", " ".join(map(str, lista_intercalada)))
main()