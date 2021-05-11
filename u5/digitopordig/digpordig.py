# Andreza Santana
# Receber um inteiro e imprimir digito por digito, desde o menos significativo

num = int(input())

divisor = 1
resultado = 0 

while True:
    resultado = num % divisor
    
    if resultado == num: break

    digito = num // divisor % 10
    divisor = divisor * 10
    
    print(digito)
