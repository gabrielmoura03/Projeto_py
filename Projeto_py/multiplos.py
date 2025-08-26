x = int(input("Digite o valor de x:"))

print(f"Multiplos de {x} entre 1 a 100:")

for n in range(1,101):
    if n % x == 0:
        print(n, end=', ')
print()
        
    





