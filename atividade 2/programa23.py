# Recebe o preço do produto
preco = float(input("Digite o preço do produto: R$ "))

# Calcula o desconto de 10%
desconto = preco * 0.10

# Calcula o novo preço
novo_preco = preco - desconto

# Mostra o resultado
print(f"Novo preço com 10% de desconto: R$ {novo_preco:.2f}")