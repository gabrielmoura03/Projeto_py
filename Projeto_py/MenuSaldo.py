
#print ("\n===BEM VINDO AO CAIXA ELETRONICO===\n")

Saldo = 1000.00

while True:
    print("\n[ MENU ]")
    print("1- Consultar Saldo")
    print("2- Depositar Dineiro")
    print("3- Sacar Dineiro")
    print("4- Sair")
        
    opcao = input("/nEscola uma opçao(1-4): ")

    if opcao == "1":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "2":
        valor = float(input("Valor a depositar:"))
        if valor > 0:
            saldo = saldo + valor
            print("Deposito realizado com sucesso!")
        else:
            print("Valor Invalido. Digite um valor positivo.")
            
    elif opcao == "3":
        valor = float(input("Valor a Sacar:"))
        if valor <= 0:            print ("Valor Invalido.")
        elif valor > saldo:
            print("Saldo insuficiente para o saque!.")
        else:
            saldo -= valor
            print("Saque realizado com sucesso!.")

    elif opcao =="4":
        print("Obrigado por usar nosso sistema. Até logo!")
        break

    else:
            print("opçao invalida. Tente Novamente")