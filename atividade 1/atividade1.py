nome = input("insira o nome do Aluno:")
nota1 = float(input("insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))

media = (nota1+nota2)/2
print("O Aluno: ",nome," Obteve a média: ",media)

if media >= 7:
    print(" Situação Final: Aprovado")

elif media >= 6:
    print(" Situação Final: Recuperação")

else:
    print(" Situação Final: Reprovado")
