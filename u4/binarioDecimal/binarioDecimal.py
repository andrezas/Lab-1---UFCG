# Andreza Santana
# Converte um valor binário para decimal

binario = input()

index = []
caractere = []
for i in range(len(binario)):
    index.append(i)
    caractere.append(binario[i])

tamanho = len(index)-1
index2 = list(range(tamanho, -1, -1))

soma = 0
for x in range(len(caractere)):
    potencia = 2**index2[x]
    decimal = int(caractere[x]) * potencia
    soma += decimal
    print(f"{caractere[x]} * {potencia} = {decimal}")
print(f"{binario}(2) = {soma}(10)")
