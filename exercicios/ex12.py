login = "Alphamage"
senha = "1234"


for tentativa in range(0, 3):

    login_input = str(input("LOGIN: "))
    senha_input = str(input("SENHA: "))

    if login == login_input and senha == senha_input:
        print("ACESSO PERMITIDO !")
        break
    else:
        print("ACESSO NEGADO !")
        if senha_input != senha:
            print("SENHA ERRADA !")
        else:
            print("LOGIN ERRADO !")


