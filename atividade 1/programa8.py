nome= (input("Digite o seu nome:"))
idade=int(input("Digite sua Idade:"))

if idade > 0 or idade < 120:
  print("Idade Inválida.")
  

else: 
  
    dias=idade*365
    print(nome,"Você já viveu cerca",dias,"dias")