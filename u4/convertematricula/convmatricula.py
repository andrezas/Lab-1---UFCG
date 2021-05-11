# Andreza Santana
# Converte a matrícula anterior para o novo formato

# E: Recebe a matrícula anterior
# P: Adiciona o 0 após o quinto dígito
# P: Substitui o n° inicial (2) por 1
# S: Exibe a saída

matricula = int(input())

resto = matricula % 10000000
substituicao = 10000000 + resto

string = str(substituicao)
adicional = ""
for i in range(len(string)):
    if i == 5:
        adicional = adicional + "0"
    adicional= adicional+ string[i]

print(adicional)
