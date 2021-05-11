# Andreza Santana
# Realiza a leitura de x,y e exibe os quadrados do intervalo entre os valores lidos

x = int(input())
y = int(input())

if x > y:
    print("---")
else:
    for i in range(x, y+1):
        quadrado = i**2
        print(f"{i} {quadrado}")
