# Andreza Santana
# Imprime todos Z(+) divisíveis por A e B simultâneamente, menores ou iguais a K.

a = int(input())
b = int(input())
k = int(input())

for i in range(a,k+1):
    if i % a == 0  and i % b == 0:
        print(i)



