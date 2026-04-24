numero = int(input("Digite o número para ver a tabuada: "))

for i in range(0, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")