n1 = int(input("1º número -> "))
n2 = int(input("2º número -> "))

if n1 == n2:
    print("Iguais")
else:
    if n1 > n2:
        print("{} > {}".format(n1, n2))
    else:
        print("{} < {}".format(n1, n2))
