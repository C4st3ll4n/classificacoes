login = "Alphamage"
senha = "1234"

login_input = str(input("LOGIN: "))
senha_input = str(input("SENHA: "))

if login == login_input and senha == senha_input:
    print("ACESSO PERMITIDO !")
else:
    print("ACESSO NEGADO !")
    if senha_input != senha:
        print("SENHA ERRADA !")
    else:
        print("LOGIN ERRADO !")
