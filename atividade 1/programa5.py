'''largura=float(input("Insira a largura do terreno em Metros: "))
altura=float(input("Insira a altura do terreno em Metros: "))

area=largura*altura
print("A área desse terreno é:",area)

cavalos=int(input("Quantos cavalos tem no haras?:"))
ferraduras=cavalos*4
print("Você vai precisar de ",ferraduras)

quantidade_paes=int(input("Número de pães que foram vendidos:"))
quantidade_broas=int(input("Número de Broas que foram vendidas:"))

total_paes = quantidade_paes * 0.12
total_broas = quantidade_broas * 1.50

total_geral = total_paes + total_broas
poupanca = total_geral * 0.10

print("Total de vendas entre pães e broas renderam:R$",total_paes+total_broas)
print("Devera guardar:R$",poupanca)
'''
nome= (input("Digite o seu nome:"))
idade=int(input("Digite sua Idade:"))

if idade > 120:
  print("Idade Inválida.")
  

else:
    dias=idade*365
    print (nome,"Você já viveu",dias,"dias")


'''
valor_litro=float(input("Digite o preço do litro do Combustível: R$"))
valor_pag=float(input("Insira o valor pago: R$"))

quantidade_litros = valor_pag / valor_litro
print("Você colocou",quantidade_litros,"litros no seu tanque")
'''