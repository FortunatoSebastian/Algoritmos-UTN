def registrar_contraseña():
    contraseña = input("Ingrese una contraseña para registrar: ").lower()
    return contraseña

def ingresar_contraseña(contraseña_guardada):
    ingreso = input("Ingrese contraseña: ").lower()
    while ingreso != contraseña_guardada:
        print("Contraseña incorrecta.")
        ingreso = input("Intenta de nuevo: ").lower()
    print("Acceso permitido")

contraseña_guardada = registrar_contraseña()

ingresar_contraseña(contraseña_guardada)