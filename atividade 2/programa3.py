camisasP=int(input("Número de Camisas P que foram vendidos: "))
camisasM=int(input("Número de Camisas M que foram vendidas: "))
camisasG=int(input("Número de Camisas G que foram vendidas: "))

valorP = camisasP * 10
valorM = camisasM * 12
valorG = camisasG * 15

valor_arrecadado = valorP + valorM + valorG


print("Total de vendas entre as Camisas: R$",valor_arrecadado)