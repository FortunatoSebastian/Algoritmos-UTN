cuentas = {"usuario1": "1234", "usuario2": "elpepe", "usuario3": "holamundo"}

try:
    login_usuario = input("Ingrese su usuario: ")
    login_contraseña = input("Ingrese su contraseña: ")

    if login_contraseña == cuentas[login_usuario]:
        print("Bienvenido")
    else:
        print("Contraseña incorrecta")
except KeyError:
    print("Error: Este usuario no existe")