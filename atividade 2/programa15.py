latas = int(input("Digite a quantidade de latas (350 ml): "))
garrafas600 = int(input("Digite a quantidade de garrafas (600 ml): "))
garrafas2L = int(input("Digite a quantidade de garrafas (2 litros): "))

total_litros = (latas * 0.35) + (garrafas600 * 0.6) + (garrafas2L * 2)

print(f"Total de refrigerante comprado: {total_litros:.2f} litros")