
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
        valor = float(input("Valor a depositar:"))
        if valor > 0:
            saldo += saldo 
            print("\nDeposito realizado com sucesso! Novo saldo {saldo:.2f}")
        else:
            print("\nValor Invalido")

    elif opcao == "2":
    
        valor = float(input("Valor a sacar: R$"))
        if valor <= saldo and valor > 0:
            saldo -= valor 
            print("\nSaque realizado com sucesso! Novo saldo {saldo:.2f}")
        elif valor <= 0:
            print("\nValor invalido. O saque")    
        else:
            print("Valor Invalido")

    elif opcao == "3":
            print(f"\nSaldo Atual: R$ {Saldo:.2f}")
       
    elif opcao =="4":
        print("\nObrigado por usar nosso sistema. Até logo!")
        break

    else:
        print("\nopçao invalida. Tente Novamente")