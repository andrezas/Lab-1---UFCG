# Andreza Santana
# Determina quantas palavras de uma sequência devem vir antes e/ou depois da palavra de referencia

quant = int(input())
palavras = []

palavras = []
for i in range(quant):
    palavras.append(input())

print('---')
referencia = input()

antes = depois = 0
for palavra in palavras:
    if palavra < referencia:
        antes += 1
    elif palavra > referencia:
        depois += 1

print(f"{antes} antes")
print(f"{depois} depois")
