# Andreza Santana
# Determina a menor sequencia no DNA

dna1 = input().upper()
dna2 = input().upper()
dna3 = input().upper()

if dna1 < dna2:
    print(dna1)

if dna1 < dna3 and len(dna1) == len(dna3):
    print(f"{dna1} {len(dna1)}")
elif dna1 < dna2 and len(dna1) == len(dna3):
    print(f"{dna1} {len(dna1)}")
elif dna2 < dna1 and len(dna2) == len(dna3):
    print(f"{dna2} {len(dna2)}")
elif dna2 < dna3 and len(dna2) == len(dna1):
    print(f"{dna1} {len(dna1)}")
elif dna3 < dna1 and len(dna3) == len(dna2):
    print(f"{dna2} {len(dna2)}")
else:
    print(f"{dna3} {len(dna3)}")
