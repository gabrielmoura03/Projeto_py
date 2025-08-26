P1 = float(input("Digite a nota da prova 1 (P1):"))
P2 = float(input("digite a nota da prova 2 (P2):"))

T1 = float(input("Digite a nota 1 do trabalo (T1):"))
T2 = float(input("Digite a nota 2 do trabalo (T2):"))


MP = (P1 + P2)/2
MT = (T1 + T2)/2
MF = 0.8*MP + 0.2*MT

print(f"Media fical:{MF:.2f}")

if MF >= 6.0:
    print("APROVADO")
else:
    print("REPROVADO")