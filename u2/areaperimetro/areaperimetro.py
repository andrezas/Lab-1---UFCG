# Andreza Santana
# Calcula área e perímetro do círculo

import math 

diametro = int(input())

raio = diametro/2
area = math.pi*((diametro/2)**2)
perimetro = 2 * math.pi*(diametro/2)

print(f"A: {area:.5f}")
print(f"P: {perimetro:.5f}")
