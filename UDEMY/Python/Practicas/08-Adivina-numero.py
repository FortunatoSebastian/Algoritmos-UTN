import random
print("Esto es un juego de adivinar numeros. \n Tienes que adivinar un numero de 1-10.")
def adivina_numero():
    secreto = random.randint(1, 10)
    intentos = int(input("Ingresa un numero: "))
    while intentos != secreto:
        print("El numero es INCORRECTO.")
        print("Prueba nuevamente....")
        intentos = int(input("Ingresa un numero: "))
        print("El numero es CORRECTO.")
        print("Felicidades")
        break
    

adivina_numero()
