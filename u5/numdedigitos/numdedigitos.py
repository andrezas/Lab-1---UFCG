# Andreza Santana
# Escreve o número de dígitos de um número lido da entrada padrão

num = int(input())
if num == 0:
    print(1)
else:
    divisor = 10
    cont = resultado = 0
    while resultado != num:
        resultado = num % divisor
        divisor = divisor * 10
        cont += 1

    print(cont)
