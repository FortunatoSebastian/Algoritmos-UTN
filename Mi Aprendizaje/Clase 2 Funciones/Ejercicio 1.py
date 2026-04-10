def describir_producto():
    nombre = input("Ingrese el nombre: ")
    precio = int(input("Ingrese el precio: "))
    disponible = True

    print(f"Nombre del Producto: {nombre}")
    print(f"Valor: ${precio}")
    if disponible == True:
        print(f"El producto esta Disponible")

describir_producto()