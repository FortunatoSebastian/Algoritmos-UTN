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
# nombre = input("Ingrese nombre: ")
# telefono = input("Ingrese telefono: ")

# cursor.execute("INSERT INTO contactos (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
# conexion.commit()
# --------------------------------------------------------------
#ESTO ES PARA BUSCAR DATOS 

cursor.execute("SELECT * FROM contactos")
filas = cursor.fetchall()

for fila in filas:
    print(fila)
# --------------------------------------------------------------
#ESTO ES LA CONECXION 
conexion.commit()
conexion.close()