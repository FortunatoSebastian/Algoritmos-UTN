import sqlite3
import os 
os.system("cls")

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        precio INTEGER)
""")

cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", ("Don satur", 1200))
conexion.commit()

cursor.execute("SELECT * FROM productos")
filas = cursor.fetchall()

for fila in filas:
    print(fila)

conexion.commit()
conexion.close()