import csv
import os
os.system("cls")
producto = input("Ingrese el nombre del producto: ")
precio = int(input("Ingrese el precio del producto: "))

archivo_nuevo = not os.path.exists("productos.csv")

with open("productos.csv", "a", newline="") as archivo:
    writer = csv.writer(archivo)
    if archivo_nuevo:
        writer.writerow(["nombre", "precio"])
    writer.writerow([producto, precio])

with open("productos.csv", "r") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila)