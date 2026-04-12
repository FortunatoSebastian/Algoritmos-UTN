productos = ["papa", "cebolla", "tomate", "banana", "manzana"]

try:
    buscar = int(input("Ingrese un numero de la posicion: "))

    print(productos[buscar])
except IndexError:
    print("Error: El indice elegido no existe")
except ValueError:
    print("Error: Tenes que ingresar un numero")