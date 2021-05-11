# Andreza Santana
# Separar as sequencias cuja as somas >= a um valor limite
# 1: Ler o valor limite
# 2: Receber as sequencias. O caractere '-' indica o fim das entradas (if: break)
# 2.1: Realizar as soma e se soma > limite adicionar a seq a uma lista 
# 2.1: (if- break) O programa para de ler quando a soma é 5x maior que o limite
# Uma linha para cada saída cujo valor >= limite

limite = int(input())

acima = []
while True:
    seq = input().split()
    if seq[0] == '-': break

    soma = 0
    for i in range(len(seq)):
        soma += int(seq[i])
    
    if soma > 5*limite: 
        acima.append(seq)
        break
    
    elif soma >= limite:
        acima.append(seq)

if len(acima) > 0:
    for lista in acima:
        resultado = ''
        somatorio = 0
        ultimo = len(lista)-1
        for j in range(len(lista)):
            somatorio += int(lista[j])
            if j == 0 and j != ultimo:
                resultado = resultado + lista[j] + ' ' + '+' + ' '
            elif j == ultimo:
                resultado = resultado + lista[j] 
            else:
                resultado = resultado + lista[j] + ' ' + '+' + ' '

        print(f"{resultado} = {somatorio}")
