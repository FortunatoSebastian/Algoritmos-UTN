import os 
os.system("cls")
1
edad = int(input("1. Ingrese su edad: "))

if edad == 18:
    print("1. Usted tiene 18 años")

2
edad_usuario = int(input("2. Ingrese su edad: "))

if edad_usuario > 18:
    print("2. Mayor")
else:
    print("2. Menor")

3
altura_jugador = float(input("3. Ingrese la altura del basquetbolista: "))

if altura_jugador > 1.80:
    print("3. El jugador si puede ser pivot")
else:
    print("3. El jugador no puede ser pivot")

4
edad_usuario = int(input("4. Ingrese su edad: "))

if edad_usuario >= 13 and edad_usuario <= 17:
    print("4. Usted es adolecente")
else:
    print("4. Usted no es adolecente")

5
edad = int(input("5. Ingrese su edad: "))

if edad >= 18:
    print("5. Usted es mayor de edad.")
elif edad <= 10:
    print("5. Usted es un niño/a.")
elif edad > 10 and edad <= 13:
    print("5. Usted es un pre-adolescente.")
elif edad > 13 and edad <= 17:
    print("5. Usted es un adolescente.")
else:
    print("5. Numero no reconocido.")