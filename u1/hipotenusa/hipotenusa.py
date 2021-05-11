#Andreza Santana
#c: cateto

import math

c1 = float(input("Medida do Cateto 1? "))
c2 = float(input("Medida do Cateto 2? "))

hipotenusa = math.sqrt((c1**2)+(c2**2))

print(f"Medida da Hipotenusa: {hipotenusa:.2f}")
