def calcular_digito(cpf, multiplicadores):
    soma = sum(int(digito) * peso for digito, peso in zip(cpf, multiplicadores))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)
def validar_cpf(cpf):
    cpf_numeros = cpf.replace('.', '').replace('-', '')
    if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
        return "Inválido"
    primeiro_digito = calcular_digito(cpf_numeros[:9], range(10, 1, -1))
    segundo_digito = calcular_digito(cpf_numeros[:9] + primeiro_digito, range(11, 1, -1))
    if cpf_numeros[-2:] == primeiro_digito + segundo_digito:
        return "Válido"
    else:
        return "Inválido"
cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
print(validar_cpf(cpf))
