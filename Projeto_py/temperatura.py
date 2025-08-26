temperatura = float(input("Digite a temperatura em graus C"))

if temperatura < 0:
    print("Frio Estremo")
elif temperatura >=0 and temperatura <= 10:
    print("Frio")
elif 11 <= temperatura <= 25:
    print("Ameno")
elif 26 <= temperatura <= 35:
    print("Quente")
else:
    print("Muito Quente")