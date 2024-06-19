import random
def main():
    num_elementos = random.randint(5, 20)
    elementos = [random.randint(1, 10) for _ in range(num_elementos)]
    print("Lista elementos:")
    print(elementos)
    print()
    soma = sum(elementos)
    media = soma / num_elementos
    print(f"Soma dos valores: {soma}")
    print(f"Média dos valores: {media:.2f}")
main()