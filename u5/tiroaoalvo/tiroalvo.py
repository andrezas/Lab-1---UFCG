# Andreza Santana
# 1: Ler ordenadas do tiro até que o sentinela seja digitado
# 2: O sentinela ou tiro de encerramento é o tiro com distância > 200cm do alvo

import math

distancia = disparos = media = soma = 0
while True:
    x, y = input().split()
    distancia = math.sqrt(float(x)**2 + float(y)**2)
    
    if distancia > 200:
        media = soma / disparos
        print("--")
        print(f"num disparos: {disparos}")
        print(f"distancia media: {media:.2f}cm")
        break

    print(f"{distancia:.2f}cm")
    disparos += 1
    soma += distancia


