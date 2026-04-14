import os
import sqlite3

conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto TEXT,
        cantidad INTEGER,
        precio INTEGER,
        total INTEGER)
""")

def registrar_venta():
    os.system("cls")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad que quiera comprar: "))
    precio = int(input("Ingrese el precio del producto: "))

    cursor.execute("INSERT INTO ventas (producto, cantidad, precio, total) VALUES (?, ?, ?, ?)", (producto, cantidad, precio, cantidad * precio))
    conexion.commit()

def ver_ventas():
    os.system("cls")
    cursor.execute("SELECT * FROM ventas")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
    input("\nPresione Enter para volver al menú...")

def total_recaudado():
    os.system("cls")
    cursor.execute("SELECT SUM(total) FROM ventas")
    resultado = cursor.fetchone()
    print(f"Total recaudado: ${resultado[0]}")
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