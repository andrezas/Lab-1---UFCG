# Andreza Santana
# Classifica letra como vogal ou consoante

palavra = input()

for i in palavra:
    if i in "AaEeIiOoUu":
        print(f"<{i}> sim")
    else:
        print(f"<{i}> nao")
