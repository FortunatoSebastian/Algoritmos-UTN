import os
import sqlite3

def iniciar_db():
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                precio INTEGER)
    """)
    conexion.commit()
    conexion.close()

def get_conexion():
    conexion = sqlite3.connect("productos.db")
    conexion.row_factory = sqlite3.Row
    return conexion


