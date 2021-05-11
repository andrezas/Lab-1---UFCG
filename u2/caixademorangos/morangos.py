# Andreza Santana
# Calcula caixas para embalar morangos

morangos = int(input())

caixas = morangos // 400
resto = morangos % 400
porcentagem = (resto*100)/morangos

print(f"Serão necessárias {caixas} caixa(s) para embalar os morangos.")
print(f"{porcentagem:.1f}% dos morangos serão perdidos.")

