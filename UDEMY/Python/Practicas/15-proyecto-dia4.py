import random

vidas = 8
numero_random = random.randint(1,20)

print("Adivina el numero")

while vidas > 0:
    numero = int(input("Ingrese un numero para adivinar: "))
    if numero == numero_random:
        print("Felicidades adivinaste el numero.")
        break
    elif numero > numero_random:
        print("El numero ingresado es mayor al numero secreto.")
    else:
        print("El numero ingresado es menor al numero secreto.")

    vidas -= 1
    print(f"te quedan {vidas} vidas faltantes.")

    if vidas == 0:
        print(f"Game over. el numero secreto era : ", numero_random)

