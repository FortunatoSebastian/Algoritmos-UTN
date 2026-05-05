from random import *

print("Buenas, bienvenido a 'Adivina el numero'")
print("Vamos a pensar un numero del 1 al 100 y tendrás 8 intentos para ganar")

numero_secreto = randint(1,100)
intentos = 0
adivinado = False

while intentos < 8 and not adivinado:
    intento = int(input("Ingresa un numero: "))
    intentos += 1
    
    if intento > numero_secreto:
        print(f"El numero ingresado es muy alto. Baja un poco más. Te quedan {8 - intentos}")
    elif intento < numero_secreto:
        print(f"El numero ingresado es muy bajo. Sube un poco más. Te quedan {8 - intentos}")
    else:
        adivinado = True
        print(f"FELICIDADES, El numero secreto era el {numero_secreto}, ganaste el juego")

if not adivinado:
    print("Game Over. Te quedaste sin intentos. Buena suerte la proxima.")
