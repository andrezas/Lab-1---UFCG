#Andreza Santana

salarioatual = float(input('Valor atual? '))
salarionovo = float(input('Novo valor? '))

reajuste = (salarionovo*100/salarioatual) - 100

print(f"Reajuste de {reajuste:.1f}%")
