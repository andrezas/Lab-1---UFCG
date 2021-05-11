# Andreza Santana
# Recebe n inteiros e calcula a soma e média dos valores pares

quantidade = int(input())

numeros = []
soma = cont = abaixo = 0
for i in range(quantidade):
    n = int(input())
    if n % 2 == 0:
        soma += n
        cont += 1
    numeros.append(n)

media = soma / cont

print(f"soma: {soma}")
print(f"média: {media:.1f}")
for numero in numeros:
    if numero < media:
        abaixo += 1
print(f"{abaixo} número(s) abaixo da média")


