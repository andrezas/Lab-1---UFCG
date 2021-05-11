# Andreza Santana
# Calcula o valor do nome

nome = input("Nome? ")
valor = float(input('Valor da letra (R$)? '))

total = len(nome)*valor

print(f"Preço final: R$ {total:.2f}")

