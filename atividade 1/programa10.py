nome= (input("Digite o seu nome:"))
idade=int(input("Digite sua Idade:"))
while True:
    if idade > 120 or idade < 0:
        print("Idade Inválida.")
        idade=int(input("Digite sua Idade:"))
    else: 
        break
dias=idade*365
print(f"Olá {nome} Você já viveu cerca",dias,"dias")