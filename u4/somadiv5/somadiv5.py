# Andreza Santana
# Soma os divisiveis por 5 entre N números

n = int(input())

soma = 0
for i in range(n):
    numero = int(input())
    if numero % 5 == 0:
        soma += numero

print(soma)
