def imprimir_multiplos(x):
    print(f"\nMultiplos de {x} entre 1 e 100:")
    for num in range(1,101):
        if num % x == 0:
            print(num, end= " ")

    print()

def main():
    x = int(input("\nDigite um número inteiro:"))

    imprimir_multiplos(x)

if __name__ == "__main__":
    main()