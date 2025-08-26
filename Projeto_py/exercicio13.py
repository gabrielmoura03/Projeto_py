

palestra_ia = set()
workshop_python = set()



        
    

def adicionar_aluno():
        nome = input("\nNome do Aluno:\n").strip()
        while nome == "":
            print("\nO nome nao pode estar vazio.\n")
            nome = input("\nNome do Aluno:\n").strip()

        evento = input("\n Evento (IA ou Pyton)\n").strip().lower()

        if evento == "ia":
            palestra_ia.add(nome)
            print(f"\n{nome} adicionado a palestra de IA.")
        elif evento == "pyton":
            workshop_python.add(nome)
            print(f"\n{nome} adicionado a palestra de Pyton")
        else:
            print("\nEvento Invalido. Digite apenas IA OU Pyton.\n ")
    
def mostrar_ambos():
        ambos = palestra_ia.intersection(workshop_python)
        print("\nAlunos que participaram de ambos os eventos:\n")

        if ambos:
            for aluno in ambos:
                print(aluno)
        else:
            print("\n Nenum aluno participou de ambos os eventos.\n")
    
def mostrar_so_ia():
            ambos = palestra_ia.difference(workshop_python)
            print("\nAlunos que participaram somente da palestra de IA :\n")

            if somente_ia:
                for aluno in somente_ia:
                    print(aluno)
            else:
                print("\n Nenum aluno participou somente da palestra de IA.\n")
    
    
def mostrar_somente_um():
    pelomenos_um = palestra_ia.union(workshop_python)
    print("\nAlunos que participaram de pelo menos um evento:\n")

    if pelomenos_um:
        for aluno in pelomenos_um:
            print(aluno)
    else:
        print("\n Nenum aluno participou de pelo menos um evento.\n")

def verificar_participacao():
    nome = input("\nDigite o nome do aluno a verificar:\n")

    em_ia = nome in palestra_ia
    em_pyton = nome in workshop_python

    if em_ia and em_pyton:
        print(f"\n{nome} participou de ambos os eventos.")

    elif em_ia:
        print(f"\n{nome}participou somente da palestra IA")

    elif em_pyton:
        print(f"\n{nome} participou somente da palestra Pyton")
    else:
        print(f"\n{nome} nao participou de nenuma palestra")



def main():
    while True:
        print("==MENU EVENTO==")
        print("1- Adicionar aluno")
        print("2- Mostrar alunos que participaram de ambos os eventos")
        print("3- Mostrar alunos que participaram somente da paletra de IA")
        print("4- Mostrar alunos que participaram somente de uma palestra")
        print("5- Verificar alunos que participaram de palestrar")
        print("6- Sair")

            

        opcao = input("Digite a opçao que deseja(1-6):")

        if opcao == "1":
            adicionar_aluno
        elif opcao == "2":
            mostrar_ambos
        elif opcao == "3":
            mostrar_so_ia
        elif opcao == "4":
            mostrar_somente_um
        elif opcao == "5":
            verificar_participacao
        elif opcao == "6":
            print("Até logo")
            break
        else:
            print("Opcao invalida. Tente novamente")




if __name__ == "__main__":
    main()