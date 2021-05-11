#Andreza Santana
#h: hora
#v: valor

nome = input()
hextra = float(input())
salariomin = float(input())
v_hextra = float(input())

salario_hextra = hextra*v_hextra
bruto = 4*salariomin+salario_hextra
inss = 0.12*bruto
imposto = 0.20*bruto
liq = bruto - (inss+imposto)

print(f"O Salário Bruto de {nome} é de R$ {bruto:.2f}")
print(f"O Salário Líquido de {nome} é de R$ {liq:.2f}")
