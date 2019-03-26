n1 = int(input("Nota 1 -> "))
n2 = int(input("Nota 2 -> "))
n3 = int(input("Nota 3 -> "))
n4 = int(input("Nota 4 -> "))

media = (n1+n2+n3+n4)/4

print("Aprovado" if media >= 6 else "Recuperação ou Reprovado")