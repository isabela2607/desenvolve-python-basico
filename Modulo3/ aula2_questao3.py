# Solicitando dados
idade = int(input('Digite a sua idade: '))
partidas_jogadas = input('Já jogou pelo menos 3 jogos de tabuleiro? (resposta deve ser True ou False)')
partidas_ganhas = int(input('Quantos jogos já venceu? '))

# Análise para inscrição
analise_idade = idade >= 16 and idade <= 18
analise_partidas = partidas_jogadas == "True"
analise_ganhos = partidas_ganhas >= 1

# Aptidão
aptos = analise_idade and analise_partidas and analise_ganhos

# Resposta
print(f"Apto para ingressar no clube de jogos de tabuleiro: {aptos}")
