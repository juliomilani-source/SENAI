# variavel =  tipo (entrada("texto: "))
altura_pessoa = float(input("Digite sua altura (em metros): "))
sombra_pessoa = float(input("Digite o tamanho da sua sombra (em metros): "))
sombra_predio = float(input("Digite o tamanho da sombra do prédio (em metros): "))

#predio vai ser igual a (altura_pessoa x sombra do predio) dividido pela altura da pessoa
altura_predio = (altura_pessoa * sombra_predio) / sombra_pessoa

# exiba (texto {variavel} metros)
print(f"A altura do prédio é: {altura_predio:.2f} metros")