# Andreza Santana
# Calcula quanto empregado e empregador devem pagar de inss

salario = float(input())

empregador = salario*(12/100)

empregado = 0

if salario < 1317.07:
    empregado = salario*(8/100)
elif salario >= 1317.07 and salario <= 2195.12:
    empregado = salario*(9/100)
elif salario > 2195.12:
    empregado = salario*(11/100)

print(f"O valor da contribuição do INSS a ser pago pelo empregador é de R$ {empregador:.2f}")
print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {empregado:.2f}")
