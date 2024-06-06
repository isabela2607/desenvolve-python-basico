# Solicita um valor
quantia= int(input( 'Escreva um valor inteiro, que irei dizer a menor quantidade de notas possivel para pagar este valor:' ))

# Calcula a quantidade de notas de R$100,00
qtd_100 = quantia // 100
quantia %= 100

# Calcula a quantidade de notas de R$50,00
qtd_50 = quantia // 50
quantia %= 50

# Calcula a quantidade de notas de R$20,00
qtd_20 = quantia // 20
quantia %= 20

# Calcula a quantidade de notas de R$10,00
qtd_10 = quantia // 10
quantia %= 10

# Calcula a quantidade de notas de R$5,00
qtd_5 = quantia // 5
quantia %= 5

# Calcula a quantidade de notas de R$2,00
qtd_2 = quantia // 2
quantia %= 2

# O restante é o número de notas de R$1,00
qtd_1 = quantia

# Imprime o resultado formatado
print(f"{qtd_100} nota(s) de R$100,00")
print(f"{qtd_50} nota(s) de R$50,00")
print(f"{qtd_20} nota(s) de R$20,00")
print(f"{qtd_10} nota(s) de R$10,00")
print(f"{qtd_5} nota(s) de R$5,00")
print(f"{qtd_2} nota(s) de R$2,00")
print(f"{qtd_1} nota(s) de R$1,00")
