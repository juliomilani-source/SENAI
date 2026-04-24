import math

def distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d

# Exemplo de uso
p1 = (1, 2)
p2 = (4, 6)

print("Distância:", distancia(p1, p2))