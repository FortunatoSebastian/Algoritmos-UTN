import sqlite3
import os
os.system("cls")

conexion = sqlite3.connect("agenda.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS contactos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        telefono TEXT)
""")
# ESTO ES PARA INGRESAR DATOS
# --------------------------------------------------------------
nombre = input("Ingrese nombre: ")
telefono = input("Ingrese telefono: ")

cursor.execute("INSERT INTO contactos (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
conexion.commit()
# --------------------------------------------------------------
#ESTO ES PARA BUSCAR DATOS 
def buscar_contacto(nombre):
    cursor.execute("SELECT * FROM contactos WHERE nombre = ?", (nombre,))
    filas = cursor.fetchall()

    for fila in filas:
        print(fila)

    if not filas:
        print("Error: El contacto no existe")
# --------------------------------------------------------------
#ESTO ES LA CONECXION 
buscar_contacto("Pedro") 
conexion.commit()
conexion.close()