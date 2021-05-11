# Andreza Santana
# Calcula dias de abastecimento de açude

capacidade = float(input('capacidade? '))
percentual = float(input('percentual hoje? '))
consumo = float(input('gasto diário? '))

volume = (capacidade*percentual)/100
dias = volume//consumo

print(f"volume: {volume:.2f}")
print(f"dias restantes: {dias:.0f}")
