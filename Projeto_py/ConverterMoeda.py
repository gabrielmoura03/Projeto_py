print("\n=== Sistema de Conversao de Moedas ===\n")
print("1 - DÓLAR")
print("2 - EURO")
print("3 - LIBRA")
print("4 - IENE")
      
opcao = int(input("Qual moeda deseja converter (1-4):"))


if opcao == 1:
    taxa = 0.19
    moeda = "Dólars"
elif opcao == 2:
    taxa = 0.19
    moeda = "Euros"
elif opcao == 3:
    taxa = 0.19
    moeda = "Libras"
elif opcao == 1:
    taxa = 25
    moeda = "Ienes"
else:
    taxa = None

if taxa is not None:
    valor_reais = float(input("Digite o valor em Reais(R$):"))
    valor_convertido = valor_reais * taxa
    print(f"\n{valor_reais:.2f} reais equivalente a {valor_convertido:.2f}{moeda}")
else:
    print("Opçao Invalida!")


    
#VALOR = float(input("Digite o valor em reais que deseja converter:"))
              
#DOLAR = VALOR*0.19
#EURO = VALOR*0.17
#LIBRA = VALOR*0.15
#IENE = VALOR*25


#print(f"O valor em dolar é: ${DOLAR}")
#print(f"O valor em Euro é: ${EURO}")
#print(f"O valor em LIBRA é: ${LIBRA}")
#print(f"O valor em IENE é: ${IENE}")