
# Registrar una venta — ingresa el producto, cantidad y precio unitario, y se guarda en ventas.csv

# Ver todas las ventas — muestra todas las ventas guardadas

# Ver el total recaudado — suma todos los totales y lo muestra
import os
import csv

def registrar_venta():
    os.system("cls")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad que quiera comprar: "))
    precio_unitario = int(input("Ingrese el precio del producto: "))

    archivo_nuevo = not os.path.exists("ventas.csv")

    with open("ventas.csv", "a", newline="") as archivo:
        write = csv.writer(archivo)
        if archivo_nuevo:
            write.writerow(["nombre", "cantidad", "precio", "total"])
        write.writerow([producto, cantidad, precio_unitario, cantidad * precio_unitario])


def ver_ventas():
    os.system("cls")
    with open("ventas.csv", "r") as archivo:
        reader = csv.reader(archivo)
        for fila in reader:            
            print(fila)
    input("\nPresione Enter para volver al menú...")

def total_recaudado():
    os.system("cls")
    total = 0
    with open("ventas.csv", "r") as archivo:
        reader = csv.reader(archivo)
        next(reader)
        for fila in reader:
            total += int(fila[3])
    print(f"Total recaudado: ${total}")
    input("\nPresione Enter para volver al menú...")
    
def menu():
    while True:
        os.system("cls")
        print("="*30)
        print("   Sistemas de facturación")
        print("="*30)
        print("1 -Registrar venta")
        print("2 -Ver ventas")
        print("3 -Ver total recaudado")
        print("4 -Salir")
        opciones = input("\nIngrese la opcion deseada: ")
        match opciones:
            case "1":
                registrar_venta()
            case "2":
                ver_ventas()
            case "3":
                total_recaudado()
            case "4":
                print("Hasta luego!")
                break

menu()