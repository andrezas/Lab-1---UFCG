#Andreza Santana

print('Análise da Turma')
print('===')
aprovados = int(input('Número de aprovados? '))
reprovados = int(input('Número de reprovados? '))

total = aprovados+reprovados
percento_r = (reprovados/total) * 100 
percento_a = (aprovados/total) * 100

print('---')
print(f"Total de alunos na turma: {total}")
print(f"Aprovados: {aprovados} = {percento_a:.1f}%")
print(f"Reprovados: {reprovados} = {percento_r:.1f}%")
