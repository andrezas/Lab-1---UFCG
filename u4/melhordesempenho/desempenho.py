# Andreza Santana
# Identifica o aluno com melhor desempenho

alunos = int(input())

desempenhos = []
for i in range (alunos):
    desempenhos.append(input())

testes = []
for desempenho in desempenhos:
    soma = 0
    for caractere in desempenho:
        if caractere == ".":
            soma += 1
    testes.append(soma)

maior = nmaior = 0
for teste in range(len(testes)):
    if testes[teste] > nmaior:
        nmaior = testes[teste]
        maior = teste+1
    elif testes[teste] == nmaior:
        maior = maior

if maior == 0:
    print(-1)
else:
    print(maior)
