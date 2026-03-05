from random import *
import os
os.system("cls")

nombre = input("Ingresa tu nombre: ")
os.system("cls")
print(f"{nombre} tienes que adivinar un numero del 1 al 100. y solo tienes 8 intentos para adivinar")
while True:
    inicio = input("Quieres comenzar?? (S/N): ").lower()
    if inicio == "n":
        print("El programa termino.")
        break

    elif inicio == "s":
        numero_secreto = randint(1,100)
        intentos = 8
        os.system("cls")
        while intentos > 0:
            numero = int(input("ingresa un numero del 1 al 100: "))
            os.system("cls")
            if numero == numero_secreto:
                print(f"Ganaste! el numero secreto es -{numero_secreto}-.")
                print("\n")
                print("El programa termino.")
                # print(f"Y te quedaban -{intentos}- intentos todavia.")
                break
            elif numero > numero_secreto:
                print(f"El numero ingresado -{numero}- es MAYOR que el numero secreto.")
            else:
                print(f"El numero ingresado -{numero}- es MENOR que el numero secreto.")

            intentos -= 1
            print(f"Te quedan -{intentos}- intentos todavia.")
 
 
        if intentos == 0:
            print(f"Te quedaste sin intentos, el numero secreto era -{numero_secreto}-")
    
    else:
        print("Opcion invalida. Ingresa (S/N)")
    break