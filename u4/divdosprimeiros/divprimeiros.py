# Andreza Santana
# Leitura dos 11 primeiros e soma de seus múltiplos (exceto o primeiro)
# Exibe a soma

primeiro = int(input())

soma = 0
for i in range(10):
    numero = int(input())
    if primeiro % numero == 0:
        soma += numero

print(soma)
