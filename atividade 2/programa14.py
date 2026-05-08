blusas = int(input("Digite a quantidade de blusas: "))

total_fio = blusas * 120
novelos = total_fio // 125

if total_fio % 125 > 0:
    novelos +=1

print(f"Total de novelos necessários: {novelos}")


"""import math

blusas = int(input("Digite a quantidade de blusas: "))

total_fio = blusas * 120
novelos = math.ceil(total_fio / 125)

print("Quantidade de novelos necessários:", novelos)"""
