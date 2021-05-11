# Andreza Santana
# Quantas senhas numéricas tem dígitos adjacentes iguais

n = int(input())

com = 0

for i in range(n):
    igual = 0
    senha = input()
    for valor in range(0,len(senha)-1):
        if senha[valor] == senha[valor+1]:
            igual += 1
    if igual > 0:
        com += 1

print(f"com: {com}")
print(f"sem: {n - com}")
