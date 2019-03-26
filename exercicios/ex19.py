tarefas_nao_realizadas = ['Ir para aula', 'Comer frutas', 'Finalizar as tarefas de casa', 'Comer vegetais', 'Ir para a academia']
tarefas_realizadas = []

valido = True

while valido:
    todas_tarefas = tarefas_nao_realizadas + tarefas_realizadas
    print("OPÇÕES: \n'/' -> Visualizar todas as tarefas"
          "\n'+' -> Adicionar uma nova tareda"
          "\n'-' -> Excluir uma tarefa realizada"
          "\n'.' -> Apresentar uma tarefa de acordo com o índice"
          "\n',' -> Apresentar tarefas realizadas"
          "\n'*' -> Apresentar a última tarefa da lista"
          "\n'#' -> Apresentar a primeira tarefa da lista"
          "\n'=' -> Apresentar tarefas com seus índices")

    op = str(input("Opção escolhida: "))

    if op.upper() == "+":
        nova_tarefa = str(input("Nova tarefa:   "))
        tarefas_nao_realizadas.append(nova_tarefa)
        print("Tarefas realizadas -> {}\nTarefas a realizar -> {}".format(tarefas_realizadas,tarefas_nao_realizadas))

    elif op.upper() == "/":
        print(todas_tarefas)

    elif op.upper() == "-":
        print("{}\nQual tarefa você deseja remover ?".format(tarefas_nao_realizadas))
        tarefa = str(input("Tarefa:   "))
        tarefas_nao_realizadas.remove(tarefa)
        tarefas_realizadas.append(tarefa)

    elif op.upper() == ".":
        indice = int(input("Indice:   "))
        print(todas_tarefas[indice])

    elif op.upper() == ",":
        print(tarefas_realizadas)

    elif op.upper() == "*":
        print(tarefas_nao_realizadas[-1])

    elif op.upper() == "#":
        print(tarefas_nao_realizadas[0])

    elif op.upper() == "=":
        print("\nTAREFAS")
        for item in tarefas_nao_realizadas:
            print("{} -> {}".format(item, tarefas_nao_realizadas.index(item)))

    print("\n")
