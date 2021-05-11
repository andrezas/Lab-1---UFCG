# Andreza Santana
# Digito verificador de conta bancária

conta = int(input())

tamanho = str(conta)
soma = 0 

for i in range(len(tamanho)):
    soma += int(tamanho[i])

verificador = soma % 11

if verificador == 10:
    print(f"{conta}-X")
else:
    print(f"{conta}-{verificador}")

