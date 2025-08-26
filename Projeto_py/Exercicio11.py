assentos = [False] *10

def reservar_assento():
    numero = int(input("\nDigite o número do assento para reserver(1 a 10)\n"))

    if 1 <= numero <= 10:
        if assentos[numero - 1] == False:
            assentos[numero - 1] = True
            print(f"\nAssento {numero} reservado com sucesso.\n")
        else:
            print(f"Assento {numero} já está ocupado.")
    else:
        print("\nNumero de Assento Inválido!\n")

def liberar_assento():
    numero = int(input("\nDigite o número do assento para liberar(1 a 10)\n"))

    if 1 <= numero <= 10:
        if assentos[numero - 1] == True:
            assentos[numero - 1] = False
            print(f"\nAssento {numero} reservado com sucesso.\n")
        else:
            print(f"Assento {numero} já está ocupado.")
    else:
        print("\nNumero de Assento Inválido!\n")

def mostrar_mapa():
    print("\n\Mapa de Ocupaçao dos Assentos:n")
    for i in range (10):
        if assentos[i] == True:
            status = "Ocupado"
        else:
            status = "Livre"
    print(f"Assento {i + 1}: {status}")
print() 


def main():
    while True:
        print("\n---Menu do Cinema---\n")
        print("\n1. Reservar um Assento\n")
        print("\n2. Liberar um Acento\n")
        print("\n3. Mostrar Mapa de Ocupaçao\n")
        print("\n4. Sair\n")

        opcao = input("\nEscolha uma opçao (1-4):\n")

        if opcao == "1":
            reservar_assento()
        elif opcao == "2":
            liberar_assento()
        elif opcao == "3":
            mostrar_mapa()
        elif opcao == "4":
            print("\nEncerrando Programa. Até logo.\n")
            break
        else:
            print("\nOpçao Invalida. Tente Novamente.\n")


if __name__ =="__main__":
    main()