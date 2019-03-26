cardapio = ['X-Eggs', 'X-Tudo', 'X-Bacon', 'Americano', 'Bauru', 'Completo', 'Pizza Broto']
escolha = str(input("Qual o seu pedido ?\n Resposta: "))

if escolha in cardapio:
    confirmar = str(input("Você confirmar o pedido ( Um {} )  ?\n Resposta (S ou N): ".format(escolha)))
    if confirmar.upper() == "S":
        print("Seu {} chegará logo".format(escolha))
    elif confirmar.upper() == "N":
        print("Faça um novo pedido")
    else:
        print("Opção inválida !")
else:
    print("\nOps, parece que seu pedido não existe no nosso cardápio"
          "\nDê uma olhada no nosso cardápio e faça um novo pedido !")
    print(cardapio)
