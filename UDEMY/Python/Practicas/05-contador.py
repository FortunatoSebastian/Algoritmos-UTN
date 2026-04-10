def contador_numeros():
    n = int(input("Ingrese un numero para contar: "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print("El resultado es: ", total)

contador_numeros()