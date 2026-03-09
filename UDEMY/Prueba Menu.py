from random import *
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

def Menu2 ():
    os.system("cls")
    while True:
        print("-" * 50)
        print("1 - Calculadora")
        print("2 - Adivina el numero")
        print("3 - Tabla de multiplicar")
        print("4 - ver perfil")
        print("5 - Salir")
        print("-" * 50)
        opciones = input("Ingrese la opcion del MENU que necesite: ")
        match opciones:
            case "1":
                calculadora()
            case "2":
                adivina_el_numero()
            case "3":
                tabla_de_multiplicar()
            case "4":
                pass
            case "5":
                print("Cerrando Sesion")
                break

def Registro():
    os.system("cls")
    while True:
        print("-" * 50)
        print("Panel de Registro de cuenta\n")
        nuevo_usuario = input("Ingrese Nombre de Usuario: ")
        nueva_contraseña = input("Ingrese Contraseña a Registrar: ")

        existe = False
        for u in usuarios:
            if u.lower() == nuevo_usuario.lower():
                existe = True
                break
        
        if existe:
            print("\nEste usuario ya existe")
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
                    print("Inicio de Sesion")
                    Menu2()
        else:
            print("Usuario o Contraseña Invalido")
            return

def calculadora():
    os.system("cls")
    while True:
        print("-" * 50)
        signo = input("Ingrese un signo para hacer el calculo ( +, -, *, / ): ")
        if signo == "salir":
            return
        if signo not in ["+", "-", "*", "/"]:
            print("\nSimbolo invalido")
            break
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

def adivina_el_numero():
    os.system("cls")
    intentos = 8
    numero_secreto = randint(1,101)
    while intentos > 0:
        print("-" * 50)
        pedir_numero = int(input("\nIngrese el numero para descubrir: "))

        if pedir_numero == numero_secreto:
            print(f"\nEncontraste el numero secreto {numero_secreto}")
            break
        elif  pedir_numero < numero_secreto:
            print("\nEl numero secreto es mas grande")    
        else:
            print("\nEl numero secreto es mas chico")
        intentos -= 1
        
        if intentos == 0:
            print(f"\nTe quedaste sin intentos. El numero secreto era: {numero_secreto}")
            break
        else:
            print(f"\nTienes: ({intentos}) intentos, sigue intentandolo")

def tabla_de_multiplicar():
    os.system("cls")
    print("Tabla de multiplicar: ")
    numero = int(input("Ingrese un numero para multiplicar"))

    for n in range(11):
        print(f"{numero} x {n} = {numero * n}")



Menu()
