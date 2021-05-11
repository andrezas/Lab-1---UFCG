# Andreza Santana
# Calcula os divisores próprios do número digitado

n = int(input())

cont = 1
for i in range(n):
    if n % cont == 0 and cont != n:
        print(cont)
    cont += 1
