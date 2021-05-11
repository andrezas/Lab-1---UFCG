# Andreza Santana
# Substitui números divisíveis ou terminados em 7

for i in range(1,103,2):
    if i % 7 == 0 or i % 10 == 7:
        i = '*'
        print(i)
    else:
        print(i)


