# Andreza Santana
# Recebe dois inteiros e indica se um deles é 10 ou a soma de ambos é 10

n1 = int(input())
n2 = int(input())

soma = n1+n2

if n1 == 10 or n2 == 10 or soma == 10:
    print('SIM')
else:
    print('NAO')
