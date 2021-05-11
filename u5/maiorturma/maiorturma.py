# Andreza Santana
# Leia um cenário de matriculas e imprima a turma com mais alunos
# Entrada consiste no nome da disciplina, seguido das matriculas
# As matriculas são interrompidas com -1
# As turmas são interrompidas com 'fim'
# A saída é o nome da turma com a quantidade de alunos

turmas = []
alunos = []

while True:
    turma = input()
    
    if turma == 'fim': break
    
    cont = 0
    while True:
        matricula = int(input())
        if matricula == -1: break
        cont += 1
    alunos.append(cont)
    turmas.append(turma)

maior = ind = 0
for i in range(len(alunos)):
    if i == 0:
        maior = alunos[i]
        ind = i
    elif alunos[i] > maior:
        maior = alunos[i]
        ind = i
if maior != 0:
    print(f"{turmas[ind]}: {maior} aluno(s)")
