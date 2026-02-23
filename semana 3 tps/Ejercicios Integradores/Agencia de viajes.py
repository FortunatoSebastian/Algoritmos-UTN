import os
os.system("cls")
nombre1 = input("Ingresar nombre del pasajero: ")
edad1 = int(input("Ingresar edad del pasajero: "))
peso1 = int(input("Ingresar peso del pasajero: "))

nombre2 = input("Ingresar nombre del pasajero: ")
edad2 = int(input("Ingresar edad del pasajero: "))
peso2 = int(input("Ingresar peso del pasajero: "))

peso_ambos_pasajeros = peso1 + peso2
precio_por_kilo = peso_ambos_pasajeros * 1000
promedio_edad = (edad1 + edad2) / 2

print(f"Hola {nombre1} y {nombre2}, sus pesos son {peso1} Kilos y {peso2} Kilos respectivamente, sumados da {peso_ambos_pasajeros}, el promedio de edad es {promedio_edad} y si viaje vale {precio_por_kilo}")