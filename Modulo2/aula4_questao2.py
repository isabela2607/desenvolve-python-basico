#Fahrenheit como um número inteiro
temperatura_fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))

#Calculando a temperatura em Celsius usando a fórmula de conversão
temperatura_celsius = int((temperatura_fahrenheit - 32) * (5/9))

#Mensagem formatada com a temperatura convertida
print(f"{temperatura_fahrenheit} graus Fahrenheit são {temperatura_celsius} graus Celsius.")
