# Andreza Santana
# Leitura de duas strings e indica em que posição o caractere da segunda string ocorre na primeira

string = input()
procurar = input()

for i in range(len(procurar)):
    for letra in range(len(string)):
        if procurar[i] == string[letra]:
            print(letra)

