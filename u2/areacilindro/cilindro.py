# Andreza Santana
# Calcula área do cilindro

import math

print('Cálculo da Superfície de um Cilindro')
print('---')
diametro = float(input('Medida do diâmetro? '))
altura = float(input('Medida da altura? '))
print('---')

bases = 2*(math.pi*((diametro/2)**2))
lateral = altura* (2*math.pi*(diametro/2))
area = bases+lateral

print(f"Área calculada: {area:.2f}")

