#Andreza Santana

orcamento_disp = float(input("Orçamento? R$ "))
adultos = int(input("Número de adultos? "))
criancas = int(input("Número de crianças? "))
pizza = float(input("Preço da pizza? R$ "))
refri = float(input("Preço do refrigerante? R$ "))
estacionamento = float(input("Preço do estacionamento? R$ "))
ingresso = float(input("Preço do ingresso do cinema? R$ "))

cinema = (adultos*ingresso)+(criancas*(ingresso/2)) + (2*(adultos+criancas))
alimentacao = pizza+refri
total = cinema + alimentacao + estacionamento
medio = total / (adultos+criancas)

print("========== Despesas do cinema ==========")
print(f"Alimentacao: R$ {alimentacao:.2f}")
print(f"Cinema: R$ {cinema:.2f}")
print(f"Custo médio por pessoa: R$ {medio:.2f}")
print(f"Total: {total:.2f}")
print(f"Saldo após passeio: {orcamento_disp - total:.2f}")
