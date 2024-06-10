distancia_entrega = float(input("Insira a distância da entrega (em quilômetros): "))
peso_pacote = float(input("Insira o peso do pacote (em quilogramas): "))
taxa_por_kg = 1.0  # valor padrão
if distancia_entrega > 100:
    if distancia_entrega > 300:
        taxa_por_kg = 2.0
    else:
        taxa_por_kg = 1.5
valor_frete = taxa_por_kg * peso_pacote
if peso_pacote > 10:
    valor_frete += 10
print("O valor do frete é R$%.2f" % valor_frete)