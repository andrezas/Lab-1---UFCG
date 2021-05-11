# Andreza Santana
# Formata a saída do cpf

n1 = int(input())
n2 = int(input())
n3 = int(input())

resto1 = n1 //100
final1 = n1 % 100
u1 = final1 % 10
d1 = final1 // 10 % 10

resto2 = n2 //100
final2 = n2 % 100
u2 = final2 % 10
d2 = final2 // 10 % 10

resto3 = n3 //100
final3 = n3 % 100
u3 = final3 % 10
d3 = final3 // 10 % 10

soma1 = u1+d1
soma2 = u2+d2
soma3 = u3+d3

print(f"{resto1}-{final1}")
print(soma1)
print(f"{resto2}-{final2}")
print(soma2)
print(f"{resto3}-{final3}")
print(soma3)

