# Andreza Santana
# Informa qual funncionário produziu mais chinelos

totais = []
nomes = []

while True:
    func = input()
    soma = 0
    if func == 'fim': break
    else:
        nomes.append(func)
        while True:
            chinelos = input()
            if chinelos == '-': break
            soma += int(chinelos)
        totais.append(soma)

maior = totais[0]
indice_func = 0
for i in range(len(totais)):
    if totais[i] > maior:
        indice_func = i

print(f'Funcionário do mês: {nomes[indice_func]}')




