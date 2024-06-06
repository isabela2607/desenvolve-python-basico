# valor do comprimento
comprimento = int(input('Digite o comprimento: '))

# valor da largura
largura = int(input('Digite a largura: '))

# valor do metro quadrado
preco_metro_quadrado = float(input('Digite o preço do metro quadrado: '))

# valor da área
area_m2 = comprimento * largura

# valor do preço total
preco_total = preco_metro_quadrado * area_m2

# Imprime o valor do terreno e suas dimensões
print(f"O valor do terreno é R${preco_total:.2f} e sua dimensão é de {area_m2}m².")