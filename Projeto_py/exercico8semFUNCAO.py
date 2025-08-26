x = int(input("Digite o valor de X (base):"))
y = int(input("Digite o valor de y (expoente):"))
        

if y == 0:
        resultado = 1
else:
    resultado = 1
    for _ in range(y): # for i in range(y):
        resultado *= x # resultado = resultado * x 

print(f"\n{x}^{y} = {resultado} ")


#resultado = 1

#for _ in range(y):
 #   resultado *= x

#print(f"\n{x} elevado a {y} tem resultado : {resultado}!")