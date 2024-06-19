def manipular_lista():
    print("Digite pelo menos 4 números inteiros (digite 'fim' para encerrar):")
    lista = []
    while True:
        valor = input()
        if valor.lower() == 'fim':
            break
        lista.append(int(valor))

    print("Lista original:", lista)
 
    print("Os 3 primeiros elementos:", lista[:3])

    print("Os 2 últimos elementos:", lista[-2:])

    print("Lista invertida:", lista[::-1])

    print("Elementos de índice par:", lista[::2])

    print("Elementos de índice ímpar:", lista[1::2])

manipular_lista()