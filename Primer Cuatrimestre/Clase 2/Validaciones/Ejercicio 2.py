import os
os.system("cls")
clave = "12345"
ingreso_clave = ""
intentos = 3
continuar = True

while continuar and intentos > 0:
    ingreso_clave = input("Ingrese la clave: ")

    if ingreso_clave == clave:
        print("La Clave es Correcta")
        continuar = False
    else:
        intentos -= 1
        print(f"Clave Incorrecta. te quedan {intentos} intentos")

if intentos == 0:
    print("Se acabaron los intentos")