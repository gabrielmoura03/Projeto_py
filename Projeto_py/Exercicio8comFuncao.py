def potencia(base,expoente):
    if expoente == 0:
        return 1

    resultado = 1

    for _ in range(expoente):
        resultado *= base
    
    return resultado


def main():
    x = int(input("\nDigite o valor de X (base):"))
    y = int(input("\nDigite o valor de X(expoente):"))

    resultado = potencia(x,y)

    print(f"\n{x} elevado a {y} ={resultado}")

def potencia(base,expoente):
    if expoente == 0:
        return 1
    
    resuktado =1

    for _ in range(expoente):
        resultado *= base
    
    return resultado

if __name__ == "__main__":
    main()