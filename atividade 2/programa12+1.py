qtd_frangos = int(input("Quantidade de frangos: "))

custo_chip = 4.0
custo_alimento = 3.50

gasto_por_frango = custo_chip + (2 * custo_alimento)
gasto_total = qtd_frangos * gasto_por_frango

print("A quantia de frangos na fazenda é de: ",qtd_frangos)
print("Para colocar a quantidade necessaria de aneis será preciso gasta: ",gasto_total)