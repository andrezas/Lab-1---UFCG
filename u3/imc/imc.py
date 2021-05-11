# Andreza Santana
# Calcula imc e classifica

peso = float(input())
altura = float(input())

imc = peso/(altura**2)

if imc < 18.5:
    print(f"IMC = {imc:.1f}")
    print(f"Classificação = Magreza")
elif 18.5 <= imc <25:
    print(f"IMC = {imc:.1f}")
    print(f"Classificação = Saudável")
elif 25 <= imc<30:
    print(f"IMC = {imc:.1f}")
    print(f"Classificação = Sobrepeso")
else:
    print(f"IMC = {imc:.1f}")
    print(f"Classificação = Obesidade")



