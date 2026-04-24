import time

tempo = 10

while tempo > 0:
    print(f"Tempo restante: {tempo} segundos")
    time.sleep(1)
    tempo -= 1

print("Prensa liberada!")

'''import time

Importa a biblioteca que permite trabalhar com tempo, como pausas.

🔹 time.sleep(1)

Faz o programa parar 1 segundo antes de continuar.

👉 Isso simula o tempo real passando.

🔹 tempo = 10

Define o tempo inicial de espera (10 segundos).

🔹 while tempo > 0

Repete enquanto o tempo for maior que zero.

🔹 tempo -= 1

Diminui 1 segundo a cada repetição.'''