contador = 1
soma = 0
while contador <= 5:
    salario = float(input(f"Digite o sálario do {contador} funcionário: "))
    contador += 1
    soma += salario
media = soma / 5    
print("A média dos sálarios dos 5 funcionários é: R$",media)
