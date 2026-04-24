# Ler o salário inicial
salario_inicial = float(input("Digite o salário do funcionário: "))

# Calcular aumento de 15%
aumento = salario_inicial * 0.15
salario_com_aumento = salario_inicial + aumento

# Descontar 8% de impostos
imposto = salario_com_aumento * 0.08
salario_final = salario_com_aumento - imposto

# Exibir resultados
print(f"Salário inicial: R$ {salario_inicial:.2f}")
print(f"Salário com aumento: R$ {salario_com_aumento:.2f}")
print(f"Salário final (com desconto de impostos): R$ {salario_final:.2f}")