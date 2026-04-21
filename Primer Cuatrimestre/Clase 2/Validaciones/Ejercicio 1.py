clave = "12345"
continuar = "si"

while continuar == "si":
    usuario = input("Ingrese la clave correcta: ")
    
    if usuario != clave:
        print("Clave incorrecta. Intentalo denuevo")
    else:
        print("La clave es correcta!.")
        continuar == "no"