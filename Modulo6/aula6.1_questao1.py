import random
def main():
    valores = [random.randint(-100, 100) for _ in range(20)]
    valores_ordenados = sorted(valores)
    print("Lista ordenada:")
    print(valores_ordenados)
    print()
    print("Lista original:")
    print(valores)
    print()
    indice_maior = valores.index(max(valores))
    indice_menor = valores.index(min(valores))
    print(f"O índice do maior valor ({max(valores)}) na lista é: {indice_maior}")
    print(f"O índice do menor valor ({min(valores)}) na lista é: {indice_menor}")
main()