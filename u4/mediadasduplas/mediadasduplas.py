# Andreza Santana
# Recebe três duplas de valores e retorna a média dos maiores valores

duplas = int(input())
maior = cont = 0
for i in range(duplas):
    n1, n2 = input().split(' ')
    if int(n1) > int(n2):
        maior += int(n1)
        cont += 1
    elif int(n2) > int(n1):
        maior += int(n2)
        cont += 1
    elif int(n1) == int(n2):
        maior += 0

if maior != 0:
    media = maior / cont
    print(f"{media:.2f}")
else:
    print('Não é possível calcular a média.')


