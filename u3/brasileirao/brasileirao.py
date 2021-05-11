# Andreza Santana
# Que time está melhor no campeonato

pontuacao1 = int(input())
vitorias1 = int(input())
marcados1 = int(input())
sofridos1 = int(input())
pontuacao2 = int(input())
vitorias2 = int(input())
marcados2 = int(input())
sofridos2 = int(input())

saldo1 = marcados1 - sofridos1
saldo2 = marcados2 - sofridos2

if pontuacao1 > pontuacao2:
    print('O Time A ganhou do Time B.')
elif pontuacao2 > pontuacao1:
    print('O Time B ganhou do Time A.')
else:
    if vitorias1 > vitorias2:
        print('O Time A ganhou do Time B.')
    elif vitorias2 > vitorias1:
        print('O Time B ganhou do Time A.')
    else:
        if saldo1 > saldo2:
            print('O Time A ganhou do Time B.')
        elif saldo2 > saldo1:
            print('O Time B ganhou do Time A.')
        else:
            print('Os dois times terminaram empatados.')

