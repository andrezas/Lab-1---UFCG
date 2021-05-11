# Andreza Santana
# Analisa variação do salário mínimo acima de U$ 100.00

inicio = int(input())
fim = int(input())

#Contador dos valores abaixo e acima de 100
abaixo = acima = somaAbaixo = somaAcima = 0
# Leitura dos salarios
for i in range(inicio, fim+1):
    salario = float(input())
    if salario > 100.00:
        acima += 1
        somaAcima += salario
    elif salario <= 100.00:
        abaixo += 1
        somaAbaixo += salario

# percentagem e media dos valores abaixo 
if abaixo != 0: 
    perc_abaixo = abaixo * 100 / ((fim+1) -inicio)
    media_abaixo = somaAbaixo / abaixo
    print(f"{abaixo} ano(s) abaixo ({perc_abaixo:.0f}% dos anos)")
    print(f"média dos anos abaixo: U$ {media_abaixo:.2f}")
else:
    print(f"{abaixo} ano(s) abaixo (0% dos anos)")

# percentagem e media dos valores acima
if acima != 0:
    perc_acima = acima * 100 /((fim+1) -inicio)
    media_acima = somaAcima / acima
    print(f"{acima} ano(s) acima ({perc_acima:.0f}% dos anos)")
    print(f"média dos anos acima: U$ {media_acima:.2f}")
else:
    print(f"{acima} ano(s) acima (0% dos anos)")

