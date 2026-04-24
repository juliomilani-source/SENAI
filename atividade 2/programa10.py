# Ler a quantidade de sanduíches
quantidade = int(input("Digite a quantidade de sanduíches: "))

# Cálculo dos ingredientes (em gramas)
queijo = quantidade * 2 * 50      # 2 fatias de 50g
presunto = quantidade * 50        # 1 fatia de 50g
carne = quantidade * 100          # 1 hambúrguer de 100g

# Converter para quilogramas
queijo_kg = queijo / 1000
presunto_kg = presunto / 1000
carne_kg = carne / 1000

# Exibir resultados
print(f"Queijo necessário: {queijo_kg:.2f} kg")
print(f"Presunto necessário: {presunto_kg:.2f} kg")
print(f"Carne necessária: {carne_kg:.2f} kg")