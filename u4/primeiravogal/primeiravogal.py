# Andreza Santana
# Realiza a leitura de uma palavra e imprime a primeira vogal

palavra = input()

vogais = []
for i in palavra:
    if i in "AEIOUaeiou":
        vogais.append(i)

if len(vogais) != 0:
    print(vogais[0])
else:
    print('-')
