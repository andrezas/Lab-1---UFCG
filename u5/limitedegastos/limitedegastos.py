# Andreza Santana
# Filtra dentre as seq de gastos as que estão acima da média estabelecida

media_mensal = float(input())

acima = []
abaixo = 0
while True:
    valores = input().split()
    soma  = 0
    if valores[0] == 'fim': break
    for i in range(len(valores)):
        soma += float(valores[i])
    media = soma / len(valores)
    if media > media_mensal:
        acima.append(valores)
    elif media*2 < media_mensal: break
    else:
        abaixo += 1

# Imprimindo resultados
#Percorre a lista de valores acima da média
for lista in acima:
    # Último elemento dentro de lista que está dentro da lista 'acima'
    ultimo = len(lista)-1
    # Resultado é a variável que vai receber os valores
    resultado = ''
    # Ajuste é a variável que vai transformar os valores para float
    ajuste = 0
    # Percorre as listas dentro da lista 'acima'
    for valor in range(len(lista)):
        if valor == 0 and valor != ultimo:
            ajuste = float(lista[valor])
            resultado = resultado + str(ajuste) + " "
        elif valor == ultimo:
            ajuste = float(lista[valor])
            resultado = resultado + str(ajuste)
        else:
            ajuste = float(lista[valor])
            resultado = resultado + str(ajuste) + " "

    if len(resultado) > 0:
        print(resultado)


