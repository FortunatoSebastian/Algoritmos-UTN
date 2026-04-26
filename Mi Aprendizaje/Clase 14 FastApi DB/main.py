from fastapi import FastAPI, HTTPException
from database import iniciar_db, get_conexion
from pydantic import BaseModel, Field

app = FastAPI()
iniciar_db()

class Producto(BaseModel):
    nombre: str = Field(min_length=2, max_length=50)
    precio: int = Field(gt=0)

#CREA UN PRODUCTO
@app.post("/productos")
def crear_producto(producto: Producto):
    conexion = get_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", 
                (producto.nombre, producto.precio))
    conexion.commit()
    conexion.close()
    return {"mensaje": "Producto creado correctamente"}

#OBTIENE LAS LISTAS DE LOS PRODUCTOS
@app.get("/productos")
def listar_productos():
    conexion = get_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    return [dict(p) for p in productos]

#BUSCA UN PRODUCTO POR ID
@app.get("/productos/{id}")
def obtener_producto(id: int):
    conexion = get_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    producto = cursor.fetchone()
    conexion.close()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return dict(producto)

#ACTUALIZA UN PRODUCTO
@app.put("/productos/{id}")
def actualizar_producto(id: int, producto: Producto):
    conexion = get_conexion()
    cursor = conexion.cursor()

    cursor.execute("UPDATE productos SET nombre = ?, precio = ? WHERE id = ?", (producto.nombre, producto.precio, id))

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    conexion.commit()
    conexion.close()
    
    return{"mensaje": "Producto actualizado"}

@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    conexion = get_conexion()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))

    if cursor.rowcount == 0: raise HTTPException(status_code=404, detail="Producto no encontrado")

    conexion.commit()
    conexion.close()

    return {"mensaje": "Producto Eliminado"}

