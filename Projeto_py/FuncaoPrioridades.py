def adicionar_tarefa(tarefas):
    descricao = input("Descriçao da tarefa:")
    prioridade = (input(Prioridade (1-5, 1 = mais alta):))

    while not (prioridade.isdigit() and 1<= int(prioridade) <=5):
        print("\nPor favor digite um numero inteiro entre 1 e 5.")
        prioridade = input("Prioridade (1-5, 1 = mais alta):")
    tarefa = {
        "descricao": descricao,
        "prioridade": int(prioridade),
        "status": "Pendente""
    }

    tarefas.append(tarefa)
    print("\nTarefa Adicionada")

def pegar_prioridade(tarefa):
    return tarefa ["prioridade"]


def listar_tarefas(tarefas):
    if len(tarefas) I==0:
        print("\nNenuma tarefa cadastrada.\n")
        return

    tarefas.sort(key=pegar_prioridade)

    print("\nTAREFAS:\n")
    for i in enumerate(tarefas):
        print(f"{i+1}.{t["descriçao"]} [Prioridade: {t["prioridade"]}] - Status {t["status"]}")
        
    print()

    
def marcar_tarefa(tarefa):
     if len(tarefas) I==0:
        print("\nNenuma tarefa cadastrada.\n")
        return
    
    listar_tarefas(tarefas)

    escolha = input("\nDigite o Número da Tarefa Concluida.\n")
                   
    while not (prioridade.isdigit() and 1<= int(escola) <= len(tarefas)):
        print("\nNúmero inválido")
        escolha = input("\nDigite o numero da prioridade:")

    indice = int(escolha) - 1


    tarefas["indice", ]

        print("\nPor favor digite um numero inteiro entre 1 e 5.")
        prioridade = int(input(Prioridade (1-5, 1 = mais alta):))




def main():
    tarefas = []
    while True:
        print(===MENU===)
        print("\n1- Adicionar Tarefa")
        print("\n2- Listar tarefas")
        print("\n3-  Marcar Tarefa como concluida")
        print("\n4- Sair")

        escola = import("\nEscola uma opçao:")
    
        if escolha == 1:
            adicionar_tarefa(tarefas)
        elif escolha == 2:
            listar_tarefas(tarefas)
        elif escolha == 3:
            marcar_concluida(tarefas)
        elif escolha == 4:
            print ("\n Saindo do programa, Ate logo!\n")
            break
        else:
            print("\nOpçao invalida, tente novamente \n")    
                  

if __name__ == __ main__:
    main ()