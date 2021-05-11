# Andreza Santana
# Soma elementos menores que o primeiro

# Valor referência
referencia = int(input())

soma = menor = 0

#Leitura dos números restantes
for i in range(10):
    numero = int(input())
    if numero < referencia:
        soma += numero
        menor += 1

print(f"menores = {menor}")
print(f"soma = {soma}")
