notas =[]

def adicionar_nota():
    nome = input("\nNome do Aluno:\n").strip()
    while nome == "":
        print("\nO nome nao pode estar vazio.\n")
        nome = input("\nNome do Aluno:\n").strip()

    nota = input("\nNota do Aluno: ").strip()
    while not nota.replace(".","").isdigit() or not (0 <= float(nota) <= 10):
        print("\n Nota Invalida, Digite um numero entre 0 e 10.\n")
        nota = input("\nNota do Aluno(0 e 10): ").strip()
        
    disciplina = input("/nDisciplina:")
    while nome == "":
        print("\nA disciplina nao pode estar vazio.\n")
        nome = input("\nDisciplina:\n").strip()

    notas.append((nome,nota,disciplina))
    print("\nNota adicionada com sucesso.\n")



def melhor_disciplina():
    if len(notas) == 0:
        print("\nNenuma Nota Cadastrada./n")
        return

    disciplinas = []

    for n in notas:
        if n[2] not in disciplinas:
            disciplinas.append(n[2])
    
    print("\nMelor aluno por disciplina: \n")

    for d in disciplinas:
        melhor_nota = -1
        melhor_aluno = ""
        for n in notas:
            if n[2] == d and n[1] > melhor_nota:
                melhor_nota = n[1]
                melhor_aluno = n[0]

        print(f"{d}: {melhor_aluno} {melhor_nota})")

def consultar_aluno():
    pass

def obter_nota(tupla):
    return tupla[1]

def exibir_ordenadas():
    if len(notas) == 0:
        print("\nNenuma Nota Cadastrada./n")
        return
    ordenadas =sorted(notas, key=obter_nota, reverse=True)

    print("\nNotas ordenadas (decrecente): \n")
          
    for n in ordenadas:
        print(f"{n[1]:.2f}, n{0}, n{2}")

def main():
    while True:
        print("\n---Menu de Notas---\n")
        print("\n1-Adicionar Nota \n")
        print("\n2-Mostrar Melores Alunos por Disciplina \n")
        print("\n3-Consultar Nota por Aluno\n")
        print("\n4-Mostrar Notas Ordenadas\n")
        print("\n5-Sair\n")

        opcao = input("Digite uma opçao (1-5:")

        if opcao =="1":
            adicionar_nota()
        elif opcao =="2":
            melhor_disciplina()
        elif opcao =="3":
            consultar_aluno()
        elif opcao =="4":
            exibir_ordenadas()
        elif opcao =="5":
            print("Encerrar Programa. Até Logo!")
            break
        else:
            print("Opçao Invalida. Tente Novamente!")
                       
            

if __name__ == "__main__":
    main()