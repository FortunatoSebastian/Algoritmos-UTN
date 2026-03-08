import os
os.system("cls")

usuarios = []
contraseñas = []
opciones = ["Registrarse", "Login", "Cerrar Sesion", "Salir"]

def Menu():
    while True: 
        os.system("cls")
        print("-" * 50)
        print("1 - Registrarse")
        print("2 - Logearse")
        print("3 - Salida")
        print("-" * 50)
        opciones = input("Ingrese la opcion del MENU que necesite: ")
        match opciones:
            case "1":
                Registro()
            case "2":
                Login()
            case "3":
                print("¡Hasta luego!")
                break
            case _:
                print("Opcion Invalida")

def Registro():
    os.system("cls")
    while True:
        print("Panel de Registro de cuenta\n")
        nuevo_usuario = input("Ingrese Nombre de Usuario: ")
        # if nuevo_usuario.lower() == "salir":
        #     print("Volviendo al Menu")
        #     return
        nueva_contraseña = input("Ingrese Contraseña a Registrar: ")

        existe = False
        for u in usuarios:
            if u.lower() == nuevo_usuario.lower():
                existe = True
                break
        
        if existe:
            print("Este usuario ya existe")
        else:
            usuarios.append(nuevo_usuario)
            contraseñas.append(nueva_contraseña)
            print("\nUsuario se registro exitosamente")
            print("-" * 50)
            return

def Login():
    
    os.system("cls")
    while True:
        print("-" * 50)
        print("Panel de Login\n")
        login_usuario = input("Ingrese Nombre de Usuario: ")
        if login_usuario.lower() == "salir":
            print("Volviendo al Menu")
            return
        login_contraseña = input("Ingrese Contraseña: ")
        for u,c in zip(usuarios, contraseñas):
            if u.lower() == login_usuario:
                if c.lower() == login_contraseña:
                    print("Ingresaste a la calculadora")
                    calculadora()
        else:
            print("Usuario o Contraseña Invalido")
            return

def calculadora():
    while True:
        print("-" * 50)
        signo = input("Ingrese un signo para hacer el calculo ( +, -, *, / ): ")
        if signo == "salir":
            return
        num1 = float(input("\nIngrese el primer valor para calcular: "))
        num2 = float(input("Ingrese el segundo valor para calcular: "))
        
        match signo.lower():
            case "+":
                resultado = num1 + num2
            case "-":
                resultado = num1 - num2
            case "*":
                resultado = num1 * num2
            case "/":
                resultado = num1 / num2
            case _:
                print("Signo invalido")
        print("-" * 50)
        print(f"El resultado de {num1} {signo} {num2} = {resultado}")

Menu()
