classe_personagem= str(input('Qual sua classe?: (guerreiro, mago ou arqueiro)'))
pontos_força= int(input('Quantos pontos de força seu personagem tem? (de 1 a 20) :'))
pontos_magia= int(input('Quantoos pontos de magia seu personagem tem?  (de 1 a 20):'))

guerreiro_a= classe_personagem=="guerreiro" and pontos_força >=15 and pontos_magia<=10
mago_a= classe_personagem=="mago" and pontos_magia >=15 and pontos_força<=10
arqueiro_a=classe_personagem=="arqueiro" and pontos_força >5 <=15 and pontos_magia  >5 <=15

print(f"Pontos de atributo consistentes com a classe escolhida: {guerreiro_a or mago_a or arqueiro_a}")