nome = input("Insira o nome do aluno:")
nota1 = float(input("Digite a primeira Nota: "))
nota2 = float(input("Digite a segunda Nota: "))
nota3 = float(input("Digite a terceira Nota: "))

media = (nota1 * 1 + nota2 * 2 + nota3 * 3) / (1 + 2 + 3)

print(f"Média ponderada: {media:.2f}")