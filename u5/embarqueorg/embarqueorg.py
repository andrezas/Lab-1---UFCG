# Andreza Santana
# Passageiros de poltronas ímpares antes das pares

# 1: Recebe uma sequencia
# 2: Criar uma nova lista da lista recebida
# 3: Verificar que segue a ordem: 1° impares e depois pares

seq = input().split()

lista = []
for i in seq:
    lista.append(i)
lista.append('2')

i = 0
while i < len(seq)-1:
    if int(seq[i]) % 2 == 0 and int(lista[i+1]) % 2 != 0:
        print('erro')
        exit()
    i += 1
print('ok')
