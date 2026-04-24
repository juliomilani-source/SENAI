# Recebe o peso da pessoa
peso = float(input("Digite o peso da pessoa (kg): "))

# Calcula os novos pesos
peso_engordar = peso * 1.15   # +15%
peso_emagrecer = peso * 0.80  # -20%

# Mostra os resultados
print(f"Peso se engordar 15%: {peso_engordar:.2f} kg")
print(f"Peso se emagrecer 20%: {peso_emagrecer:.2f} kg")