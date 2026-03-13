contador=1
soma_nota=0

while contador <= 4:
    nota = float (input(f"Digite a nota do { contador } bimestre:"))
    if nota < 0 or nota > 10:
        print("Nota Inválida. A nota deve estar entre 0 e 10.")
        continue
    contador += 1
    soma_nota += nota

media = soma_nota/4

print("O Aluno Obteve a média: ",media)

if media >= 7:
    print(" Situação Final: Aprovado")

elif media >= 5:
    print(" Situação Final: Recuperação")

else:
    print(" Situação Final: Reprovado")