
n = float(input("Digite o valor de n: "))

maior = 0 

while n > 0: 
    x = float(input("Digite o valor de x: "))
    if x > maior: 
        maior = x 
        n -= 1 
print("O maior valor registrado é:", maior)