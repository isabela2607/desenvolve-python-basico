n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

m = (n1 + n2 + n3) / 3

if m >= 60:
    print("Aprovado")
    print("Fim")
elif m >= 40:
    print("Recuperação")
    print("Fim")
else:
    print("Reprovado")
    print("Fim")