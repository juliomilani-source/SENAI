# Ler quantidade de horas trabalhadas
horas_normais = float(input("Digite as horas normais trabalhadas: "))
horas_extras = float(input("Digite as horas extras trabalhadas: "))

# Valores por hora
valor_normal = 10
valor_extra = 15

# Calcular salário bruto
salario_bruto = (horas_normais * valor_normal) + (horas_extras * valor_extra)

# Calcular desconto de 10%
imposto = salario_bruto * 0.10

# Salário líquido
salario_liquido = salario_bruto - imposto

# Exibir resultados
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")