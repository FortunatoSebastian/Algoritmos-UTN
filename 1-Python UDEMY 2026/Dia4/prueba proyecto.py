from random import *
import os 
os.system("cls")

#ENTRADAS
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre} tienes que adivinar el numero secreto")

intentos = 8
numero_secreto = randint(1,10)

#PROCESOS
while intentos > 0:
    pedir_un_numero = int(input("Ingrese un numero para descubrir el numero secreto: "))
    os.system("cls")
    if pedir_un_numero < numero_secreto:
        print(f"El numero ingresado ({pedir_un_numero}) es MENOR que el numero secreto, prueba un numero mas Grande.")
        intentos -= 1
        print(f"Tienes {intentos} intentos, sigue intentandolo.")
    elif pedir_un_numero > numero_secreto:
        print(f"El numero ingresado ({pedir_un_numero}) es MAYOR al numero secreto, prueba un numero mas Chico.")
        intentos -= 1
        print(f"Tienes {intentos} intentos, sigue intentandolo.")
    
    if pedir_un_numero == numero_secreto:
        print(f"Perfecto le atinaste al numero secreto:  {numero_secreto}")
        break
    if intentos == 0:
        print(f"Te quedaste sin intentos. El numero secreto era :{numero_secreto}.")



#         
#     
#
#SALIDA