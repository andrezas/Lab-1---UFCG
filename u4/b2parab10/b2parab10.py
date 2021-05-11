# Andreza Santana
# Binário para decimal

n = input()

indices = []
caractere = []
for i in range(len(n)):
    indices.append(i)
    caractere.append(n[i])

tamanho = len(indices)-1
indices2 = list(range(tamanho, -1, -1))

soma = 0
for x in range(len(caractere)):
    potencia = 2**indices2[x]
    decimal = int(caractere[x]) * potencia
    soma += decimal
    print(f"{caractere[x]} * {potencia} = {decimal}")
print(f"{n}(2) = {soma}(10)")
