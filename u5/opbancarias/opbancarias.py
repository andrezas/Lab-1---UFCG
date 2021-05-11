# Andreza Santana
# Programa que realiza operações bancárias

cliente = input().split()
saldo = float(cliente[1])

while True:
    operacao = input().split()
    if operacao[0] == "3":
        print(f"Saldo de R$ {saldo:.2f} na conta de {cliente[0]}")
        break
    elif operacao[0] == "1":
        saldo = saldo - float(operacao[1])
    elif operacao[0] == "2":
        saldo = saldo + float(operacao[1])


