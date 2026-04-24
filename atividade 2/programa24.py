# Recebe os dados
salario_fixo = float(input("Digite o salário fixo: R$ "))
vendas = float(input("Digite o valor das vendas: R$ "))

# Calcula a comissão (4%)
comissao = vendas * 0.04

# Calcula o salário final
salario_final = salario_fixo + comissao

print(f"Comissão: R$ {comissao:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")