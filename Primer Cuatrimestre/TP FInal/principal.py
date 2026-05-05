import os
os.system("cls")

user = "admin123"
password = "123"
inicio_sesion = False
intentos = 3

#Inicio de Sesion
while intentos > 0:
    print("="* 30)
    usuario = input("\nIngrese su usuario: ")
    contraseña = input("Ingrese su contaseña: ")

    if usuario == user and contraseña == password:

        print("Iniciando Sesion!...")
        inicio_sesion = True
        break
    else:
        print("Usuario o Contraseña incorrectos...\n")
        intentos -= 1
        print(intentos)
        if intentos == 0:
            print("Te quedaste sin intentos, acceso denegado.")
            input("Presione Enter para salir....")    


#Menu Principal
if inicio_sesion == True:
    salir = False
    while salir == False:
        os.system("cls")
        print("-----Bienvenido al Sistema de procesamiento de datos-----")
        print("="* 40)
        print("1- Proyectos")
        print("2- Tablas")
        print("3- Variables")
        print("4- Mostrar")
        print("5- Estadística")
        print("6- Salir")
        print("="*30)
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                print("Sección proyectos")
            case "2":
                print("Sección tablas")
                
            case "3":
                print("Sección variables")
                
            case "4":
                print("Mostrar")
                
            case "5":
                print("sección de estadistica")
            case "6":
                print("Salistes del programa.")
                salir = True
            case _:
                print("Opción invalida. Seleccione una opción")
        input("Presiones Enter para volver al Menu...")        