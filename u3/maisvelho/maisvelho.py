# Andreza Santana
# Recebe o nome e duas datas de nascimento e determina qual o mais vellho

nome1 = input()
dia1 = int(input())
mes1 = int(input())
ano1 = int(input())
nome2 = input()
dia2 = int(input())
mes2 = int(input())
ano2 = int(input())

if ano1 != ano2:
    if ano1 < ano2:
        print(nome1)
    elif ano2 < ano1:
        print(nome2)
elif ano1 == ano2:
    if mes1 < mes2:
        print(nome1)
    elif mes2 < mes1:
        print(nome2)
    else:
        if dia1 < dia2:
            print(nome1)
        elif dia2 < dia1:
            print(nome2)
        else:
            print('nenhuma')
