# Andreza Santana
# Avalia o desempenho do docente e indica se ele pode ou não ser promovido

semestre = int(input())
ensino = int(input())
intelectual = int(input())
orientacao = int(input())
administrativa = int(input())

media = (ensino + intelectual + orientacao + administrativa)/4

if semestre < 4:
    print("Promoção indeferida. Número de semestres insuficiente.")
else:
    if ensino < 320 or intelectual < 100 or orientacao < 20:
        print("Promoção indeferida. Pontuação mínima não alcançada.")
    elif media < 140:
        print("Promoção indeferida. Média insuficiente.")
    else:
        print("Promoção deferida. Parabéns!")
