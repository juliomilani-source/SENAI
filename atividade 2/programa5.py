def converter_tempo(dias_totais):
    anos = dias_totais // 365
    resto = dias_totais % 365
    
    meses = resto // 30
    dias = resto % 30
    
    return anos, meses, dias

dias = int(input("Digite o número de dias: "))

anos, meses, dias_restantes = converter_tempo(dias)

print(f"{anos} ano(s), {meses} mes(es) e {dias_restantes} dia(s)")