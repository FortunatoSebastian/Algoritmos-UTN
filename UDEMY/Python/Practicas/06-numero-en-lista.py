def numero_lista():
    lista = [2, 4, 7, 8, 12, 20, 48, 100, 150]
    numero = int(input("Ingresa numero para buscar en la lista: "))
    if numero in lista:
        print("El numero esta en la lista")
    else:
        print("El numero NO esta en la lista")

numero_lista()
    