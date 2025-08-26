tarefas = []

def adicionar_tarefa():
    tarefa = input("\nDigite a nova tarefa: ")

    if tarefa:
        tarefas.append(tarefa)
        print("\nTarefa adicionada com sucesso!\n")
    else:
        print("\nTarefa nao pode ser vazia.\n")


def listar_tarefas():
    if tarefas:
        print("\nLista de Tarefas:\n")
        indice = 1
        for tarefa in tarefas:
            print(f"{indice}. {tarefa}" )
            indice += 1
    else:
        print("\nNenhuma Tarefa Cadastrada.\n")

def remover_tarefa():
    nome = input("\nDigite o nome exato da tarefa que deseja remover:")

    if nome in tarefas:
        tarefas.remove(nome)
        print("\nTarefa Removida com Sucesso!\n")
    else:
        print("\nTarefa Nao Encontrada\n")

def main():
    while True:
        print("\nMenu de Tarefas\n")
        print("1. Adicionar uma nova tarefa")
        print("2. Remover uma tarefa pelo nome")
        print("3. Sair")
    
        opcao = input("\n Escolha uma opcao (1-4):")
    
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("\nEncerrando o programa. Até mais!\n")
            break
        
        else:
            print("\nOpçao invalida! Tente novamente.\n")

if __name__ == "__main__":
    main()