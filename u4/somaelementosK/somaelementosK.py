# Andreza Santana
# Leia  k e n (inteiros) e imprimir a soma dos elementos lidos a cada k posições (leituras)

k = int(input())
n = int(input())

numeros = []
for i in range(n):
    numeros.append(int(input()))

soma = 0
for numero in range(0, len(numeros), k):
    soma += numeros[numero]

print(f"Soma: {soma}.")
