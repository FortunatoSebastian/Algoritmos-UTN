import os
os.system("cls")
1.
toneladas = float(input("Ingrese la cantidad de toneladas que necesita para la construccion: "))
kilogramos = toneladas * 1000
camiones = kilogramos / 3500

if kilogramos % 3500 != 0:
    camiones = int(camiones) + 1

print("cantidad de camiones necesarios: ", int(camiones))

2.
kilometros = float(input("Ingrese la cantidad de kilometros que recorre el camion: "))
horas = kilometros / 90


print(f"El tiempo que tarda cada uno de los camiones es de {horas:.2f} horas")
