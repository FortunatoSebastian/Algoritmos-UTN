# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot
# Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota
#  es ...
import os 
os.system("cls")
#1
altura_jugador = int(input("Ingrese su altura: "))

if altura_jugador < 160:
    print(f"Posicion: base")
elif altura_jugador < 180:
    print(f"Posicion: Escolta")
elif altura_jugador < 200:
    print(f"Posicion: Alero")
else:
    print("Posicion: Pívot")

