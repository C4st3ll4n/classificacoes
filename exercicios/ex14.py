def adicao(n1a, n2a):
    return n1a + n2a


def subtracao(n1s, n2s):
    return n1s - n2s


def divisao(n1d, n2d):
    return n1d / n2d


def multiplicacao(n1m, n2m):
    return n1m * n2m


while True:

    n1 = int(input("1º número -> "))
    n2 = int(input("2º número -> "))

    op = str(input(("\nSELECIONE UMA OPERAÇÃO ARITIMÉTICA\n"
                    "     + -> SOMAR\n"
                    "     - -> SUBTRAIR\n"
                    "     * -> MULTIPLICAR\n"
                    "     / -> DIVIDIR\n"
                    "     X -> FINALIZAR\n"
                    "OPÇÃO: ")))

    if op.upper() != "X":
        if op == "+":
            print(adicao(n1, n2))
        if op == "-":
            print(subtracao(n1, n2))
        if op == "*":
            print(multiplicacao(n1, n2))
        if op == "/":
            print(divisao(n1, n2))
    else:
        print("FIM")
        break
