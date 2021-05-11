# Andreza Santana
# Ler dados de extrato do cliente e apontar a primeira op não autorizada

# 1: Op não autorizada: deposito > 1000, saque = (saldo < 0), saque = limite
# 2: Ler o limite de saques e saldo atual
# 3: Ler operações até que uma op não autorizada seja efetuada e imprimir uma mensagem identificando essa operação

limite = int(input())
saldo = float(input())

saque = deposito = valor = 0

while True:
    operacao = input().split()
    
    if operacao[0] == 'saque':
        saque += 1
        if saque > limite:
            print(f"Operação inválida: saque {float(operacao[1]):.2f}.")
            print(f"Seu saldo é R$ {saldo:.2f}.")
            break
        else:
            valor = saldo - float(operacao[1])
            if valor < 0:
                print(f"Operação inválida: saldo {float(operacao[1]):.2f}.")
                print(f"Seu saldo é R$ {saldo:.2f}.")
                break
            else:
                saldo = valor

    elif operacao[0] == 'depósito':
        if float(operacao[1]) > 1000:
            print(f"Operação inválida: depósito {float(operacao[1]):.2f}.")
            print(f"Seu saldo é R$ {saldo:.2f}.")
            break
        else:
            saldo = saldo + float(operacao[1])
