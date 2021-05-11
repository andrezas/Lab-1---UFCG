# Andreza Santana
# Calcula quantidade e valor de defensivos agrícolas

tipo = input()
area = float(input())

quantidade = 0
valor = 0
if tipo == 'Fungicida':
    quantidade = area*1.0
    valor = quantidade * 320
elif tipo == 'Herbicida':
    quantidade = area*0.3
    valor = quantidade * 100
elif tipo == 'Inseticida':
    quantidade = area*2.5
    valor = quantidade * 400


print(f"{quantidade} {tipo}(s). {valor:.2f} reais.")
