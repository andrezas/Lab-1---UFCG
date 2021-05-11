# Andreza Santana
# Calcula areas de 4 figuras planas

import math

figura = input()

area = 0
if figura == "círculo":
    raio = float(input())
    area = math.pi*(raio**2)
    print(f"Área do círculo: {area:.2f} (cm2)")
elif figura == "quadrado":
    lado = float(input())
    area = lado*lado
    print(f"Área do quadrado: {area:.2f} (cm2)")
elif figura == "triângulo":
    base = float(input())
    altura = float(input())
    area = (base*altura)/2
    print(f"Área do triângulo: {area:.2f} (cm2)")
elif figura == "retângulo":
    base = float(input())
    altura = float(input())
    area = base*altura
    print(f"Área do retângulo: {area:.2f} (cm2)")
    



