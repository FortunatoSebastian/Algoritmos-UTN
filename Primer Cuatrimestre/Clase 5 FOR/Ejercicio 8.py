numero = int(input("Ingrese un numero: "))

for n in range(1, numero + 1):
    for x in range(1, n + 1):
        print(x, end="")
    print()