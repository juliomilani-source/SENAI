# Ler valor total da conta
total = float(input("Digite o valor total da conta: R$ "))

# Dividir por 3
parte = total / 3

# Carlos e André não pagam centavos (arredondar para baixo)
carlos = int(parte)
andre = int(parte)

# Felipe paga o restante
felipe = total - (carlos + andre)

# Exibir resultados
print(f"Carlos deve pagar: R$ {carlos:.2f}")
print(f"André deve pagar: R$ {andre:.2f}")
print(f"Felipe deve pagar: R$ {felipe:.2f}")