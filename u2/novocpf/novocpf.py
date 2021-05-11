# Andreza Santana
# Recebe três partes do cpf e formata para a exibição usual

parte1 = int(input())
parte2 = int(input())
parte3 = int(input())

n1 = parte3 // 100 
n2 = (parte3 - (100*n1)) // 10
n3 = (parte3 - (100*n1)) - (n2*10)

soma = n1+n2+n3 

print(f"{parte1:03}.{parte2:03}.{parte3:03}-{soma:02}")
