#Andreza Santana

peso = float(input())
altura = float(input())

imc = peso/altura**2
imc_ideal = 24.9 * peso/ imc
peso_ideal = imc_ideal - peso

print(f"IMC atual = {imc:.2f}")
print(f"Peso a ser ganho/perdido = {peso_ideal:.2f}")
