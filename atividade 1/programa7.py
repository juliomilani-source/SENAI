quantidade_paes=int(input("Número de pães que foram vendidos:"))
quantidade_broas=int(input("Número de Broas que foram vendidas:"))

total_paes = quantidade_paes * 0.12
total_broas = quantidade_broas * 1.50

total_geral = total_paes + total_broas
poupanca = total_geral * 0.10

print("Total de vendas entre pães e broas renderam:R$",total_paes+total_broas)
print("Devera guardar:R$",poupanca)