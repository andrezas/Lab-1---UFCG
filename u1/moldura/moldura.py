# Andreza Santana
# Calcula moldura

comprimento = float(input())
largura = float(input())

c = comprimento / 100
l = largura / 100

valor = 2*((c+l)*120)

print(f"R$ {valor}")
