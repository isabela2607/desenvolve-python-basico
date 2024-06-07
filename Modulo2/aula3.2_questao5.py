genero= str(input('Seu gênero: (M ou F)'))
idade= int(input('Sua idade: '))
tempo_servico= int(input('Anos de serviço: (em anos)'))

aposentadoria = (genero == "F" and (idade > 60 or (idade >= 60 and tempo_servico >= 25))) or  (genero == "M" and (idade > 65 or tempo_servico >= 30))

print("Você já pode se aposentar?" , aposentadoria)