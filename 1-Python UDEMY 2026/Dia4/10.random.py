from random import *
import os
os.system("cls")


# aleatorio = randint(1,50)
# print(aleatorio)

# colores = ["azul","rojo","verde","amarillo"]
# aleatorio = choice(colores)
# print(aleatorio)

numeros = list(range(5,50,5))

shuffle(numeros)
print(numeros)