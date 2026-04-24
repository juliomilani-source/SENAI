peso = float(input("Digite o peso do prato (kg): "))
valor = peso * 12.0

while valor < 0:

    peso = float(input("Digite novamente o peso do prato do cliente (em Quilos) sme valores negativos"))
    print(f"Valor a pagar: R$ {valor:.2f}")