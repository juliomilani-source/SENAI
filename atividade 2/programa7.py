# Ler número inteiro (até 3 dígitos)
numero = int(input("Digite um número (até 3 dígitos): "))

# Garantir que seja positivo (caso digitem negativo)
numero = abs(numero)

# Separar os dígitos
centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

# Exibir resultado
print(f"CENTENA = {centena}")
print(f"DEZENA = {dezena}")
print(f"UNIDADE = {unidade}")