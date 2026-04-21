from fastapi import FastAPI
from database import iniciar_db, get_conexion
from pydantic import BaseModel

app = FastAPI()
iniciar_db()

class Producto(BaseModel):
    nombre: str
    precio: int


@app.post("/productos")
def crear_producto(producto: Producto):
    conexion = get_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", 
                (producto.nombre, producto.precio))
    conexion.commit()
    conexion.close()
    return {"mensaje": "Producto creado correctamente"}

@app.get("/productos")
def listar_productos():
    conexion = get_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    return [dict(p) for p in productos]