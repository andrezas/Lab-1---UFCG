# Andreza Santana
# Quantas PAs

razao = int(input())

eh_pa = anterior = 0

while True:
    pa = input().split()
    if pa[0] == 'fim':
        break
    else:
        cont = 0
        for i in range(len(pa)-1):
            anterior = int(pa[i]) + razao
            if anterior == int(pa[i+1]):
                cont += 1
        if cont+1 == len(pa):
            eh_pa += 1
print(eh_pa)

