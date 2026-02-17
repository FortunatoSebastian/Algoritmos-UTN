print("MENU DE OPCIONES")
print("[1] ventas")
print("[2] soporte")
print("[3] administracion")
opcion = int(input("Elegir opcion: "))

match opcion:
    case 1:
        print("VENTAS")
    case 2:
        print("SOPORTE")    
    case 3:
        print("ADMINISTRACION")
    case _:
        print("opcion inexistente")