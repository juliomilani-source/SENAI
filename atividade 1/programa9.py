valor_litro=float(input("Digite o preço do litro do Combustível: R$"))
valor_pag=float(input("Insira o valor pago: R$"))

quantidade_litros = valor_pag / valor_litro
print("Você colocou",quantidade_litros,"litros no seu tanque")
