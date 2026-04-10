def validar_contraseña():
    contraseña_correcta = "elpepe123"
    ingreso = input("Ingrese Contraseña: ")
    while ingreso != contraseña_correcta:
        print("Contraseña incorrecta.")
        ingreso = input("Intenta de nuevo: ")
    print("Acceso Permitido")

validar_contraseña()