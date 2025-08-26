estoque = {}


def adicionar_livro():
   
    titulo = input("\nDigite o nome do Livro\n").strip()
    while titulo == "":
        print("\nO Nome do Livro nao pode estar vazio\n")
        titulo = input("digite o nome do livro").strip()

    qtd = int(input("\nQuantidade a adicionar:")) 
   

    if titulo in estoque:
        estoque[titulo] += qtd
    else:
        estoque[titulo] = qtd
        print(f"\n{qtd} unidade(s) de {titulo} adicionada(s).\n")

    



def remover_livro():
    titulo = input("\nTitulo no estoque.\n")

    if titulo not in estoque:
            print("\nLivro nao encontrado no estoque.\n")
            return
    
    qtd = int(input("\nQuantidade a remover: "))

    if qtd > estoque[titulo]:
        print(f"\nnao a unidades suficientes para remover.")
        return
    
    estoque[titulo] -= qtd

    print(f"\n{qtd} unidade(s) removidas(s) de {titulo} .")

    if estoque[titulo] == 0:
        print(f"\n Estoque do livro {titulo} zerado.\n")



def consultar_quantidade():
    titulo = input("\nTitulo do Livro: ").strip()

    if titulo in estoque:
        print(f"\nQuantidade disponivel de {titulo}:{estoque[titulo]}")
    else:
        print("\nLivro nao esta no estoque.\n")


def mostrar_estoque():
    if not estoque:
        print("\n Estoque vazio\n")
        return
    print("\nLivro em estoque:\n")
    for titulo in sorted(estoque.keys()):
        print(f"\n{titulo}:{estoque[titulo]}\n")






def main():
    while True:

        print("1- Adicionar um livro ao estoque")
        print("2- remover um livro do estoque")
        print("3- Consultar quantidade de um livro")
        print("4- Mostrar todos os livros")
        print("5- Sair")

        opcao = input("\nDigite uma opçao válida(1-5)\n")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            remover_livro()
        elif opcao == "3":
            consultar_quantidade()
        elif  opcao == "4":
            mostrar_estoque()
        elif opcao == "5":
            print("Finalizando o programa.Até Logo")
            break
        else:
            print("Opçao Invalida, digite uma opçao entre (1 -5)")
        




if __name__ == "__main__":
    main()