import random

# aleatorio = random.randint(1,20)
# print(aleatorio)

# colores = ['azul','rojo','celeste','amarillo']
# aleatorio = random.choice(colores)
# print(aleatorio)


numeros = list(range(5,50,5))
random.shuffle(numeros)
print(numeros)