# Andreza Santana
# Conta as ocorrências em que o vizinho da direita tem valor igual

lista = []
lista = input().split(" ")

cont = 0

for i in range(len(lista)-1):

    if lista[i] == lista[i+1]:
        cont += 1

print(cont)
