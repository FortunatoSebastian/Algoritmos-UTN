import random
import os 
os.system("cls")
# 1
# edad = int(input("1. Ingrese su edad: "))

# if edad == 18:
#     print("1. Usted tiene 18 años")

# 2
# edad_usuario = int(input("2. Ingrese su edad: "))

# if edad_usuario > 18:
#     print("2. Usted es mayor de edad")

# 3
# edad_usuario = int(input("2. Ingrese su edad: "))

# if edad_usuario > 18:
#     print("2. Usted es mayor de edad")
# else:
#     print("2. Usted es menor de edad")

# 4
# altura_jugador = float(input("3. Ingrese la altura del basquetbolista: "))

# if altura_jugador > 1.80:
#     print("3. El jugador si puede ser pivot")
# else:
#     print("3. El jugador no puede ser pivot")

# 5
# edad_usuario = int(input("4. Ingrese su edad: "))

# if edad_usuario >= 13 and edad_usuario <= 17:
#     print("4. Usted es adolecente")

# 6
# edad_usuario = int(input("4. Ingrese su edad: "))

# if edad_usuario >= 13 and edad_usuario <= 17:
#     pass
# else:
#     print("usted no es adolescente.")

# 7
# edad = int(input("5. Ingrese su edad: "))

# if edad >= 18:
#     print("5. Usted es mayor de edad.")
# elif edad <= 10:
#     print("5. Usted es un niño/a.")
# elif edad > 10 and edad <= 13:
#     print("5. Usted es un pre-adolescente.")
# elif edad > 13 and edad <= 17:
#     print("5. Usted es un adolescente.")
# else:
#     print("5. Numero no reconocido.")

# 8
# altura_jugador = float(input("Ingrese su altura: "))

# if altura_jugador < 1.60:
#     print(f"Tu altura es: {altura_jugador}, Vas a jugar en la posicion de |Base|.")

# elif altura_jugador >= 1.60 and altura_jugador <= 1.79:
#     print(f"Tu altura es: {altura_jugador}, Vas a jugar en la posicion de |Escolta|.")

# elif altura_jugador >= 1.80 and altura_jugador <= 1.99:
#     print(f"Tu altura es: {altura_jugador}, Vas a jugar en la posicion de |Alero|.")

# elif altura_jugador >= 2.00:
#     print(f"Tu altura es: {altura_jugador}, Vas a jugar en la posicion de |Ala-Pívot|.")

#9
# Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos naturalizados desde los dieciocho (18) años están habilitados a votar. A partir del ingreso de la edad del usuario y el estado (si es naturalizado o nativo), se deberá informar si es o no posible que la persona concurra a votar en base a la información suministrada.

edad_usuario = int(input("Ingrese su edad: "))
estado_civil = input("Ingrese su estado civil: ").lower()

if edad_usuario >= 16 and estado_civil == "nativo":
    print(f"")

#11
# numero_aleatorio = random.randint(1,10)
# print(numero_aleatorio)
#12

# notas_aleatorias = random.randint(1,10)

# if notas_aleatorias >= 6 and notas_aleatorias <= 10:
#     print(f"Promocion directa la nota es: {notas_aleatorias}")
# elif notas_aleatorias >= 4 and notas_aleatorias <= 5:
#     print(f"Aprobado, la nota es: {notas_aleatorias}")
# elif notas_aleatorias < 4:
#     print(f"Reprobado, la nota es: {notas_aleatorias}")

