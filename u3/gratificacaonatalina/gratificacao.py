# Andreza Santana
# Informa gratificação do funcionário de acordo com salário e dias trabalhados

cod = int(input())
if cod == 1 or cod == 2:
    if cod == 1:
        salario = 25000.000
        print(f"Deverá receber em dezembro R$ {salario:.2f}.")
    elif cod == 2:
        salario = 15000.000
        print(f"Deverá receber em dezembro R$ {salario:.2f}.")
else: 
    faltas = int(input())
    if cod == 3:
        if faltas == 0:
            gratificacao = 500
            salario = 8000.000 + gratificacao
            print(f"Valor da gratificação R$ {gratificacao:.2f}.")
            print(f"Deverá receber em dezembro R$ {salario:.2f}.")
        else:
            gratificacao = (235 - faltas) * 2
            salario = 8000.000 + gratificacao
            print(f"Valor da gratificação R$ {gratificacao:.2f}.")
            print(f"Deverá receber em dezembro R$ {salario:.2f}.")
    elif cod == 4:
        if faltas == 0:
            gratificacao = 300
            salario = 5000.000 + gratificacao
            print(f"Valor da gratificação R$ {gratificacao:.2f}.")
            print(f"Deverá receber em dezembro R$ {salario:.2f}.")
        else:
            gratificacao = (235 - faltas) * 1
            salario =5000.000 + gratificacao
            print(f"Valor da gratificação R$ {gratificacao:.2f}.")
            print(f"Deverá receber em dezembro R$ {salario:.2f}.")
    elif cod == 5:
        if faltas == 0:
            gratificacao = 200
            salario = 2800.000 + gratificacao
            print(f"Valor da gratificação R$ {gratificacao:.2f}.")
            print(f"Deverá receber em dezembro R$ {salario:.2f}.")
        else:
            gratificacao = (235 - faltas) * 0.7
            salario = 2800.000 + gratificacao
            print(f"Valor da gratificação R$ {gratificacao:.2f}.")
            print(f"Deverá receber em dezembro R$ {salario:.2f}.")
