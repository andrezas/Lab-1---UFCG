# Andreza Santana
# Identificar e printar frase com maior palavra

cont = numfrase = 0

while True:
    frase = input().split()
    if frase[0] == "fim": break
    
    cont += 1
    
    if cont == 1: 
        numfrase = cont
        maior = frase[0]

    for i in range(len(frase)):
        if len(frase[i]) > len(maior):
            maior = frase[i]
            numfrase = cont
           

print(f"Frase {numfrase}: {maior}")

