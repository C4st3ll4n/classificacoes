op = str(input("VOCÊ DESEJA:\n"
               "ADICIONAR UM NOME -> +\n"
               "SAIR -> X\n"
               "OPÇÃO ESCOLHIDA = "))

lista = []
valido = True

while valido:

    if op.upper() == "X":
        print(lista)
        valido = False

    elif op.lower() == "+":

        nome = str(input("NOME :   "))
        lista.append(nome)
        op2 = str(input("DESEJA PARAR ? [S ou N]\n Resposta -> "))

        if op2.upper() == "S":
            lista.sort()
            print(lista)
            lista.sort(reverse=True)
            print(lista)
            break

        else:

            pass

    else:

        print("OPÇÃO INVÁLIDA")
        valido = False
