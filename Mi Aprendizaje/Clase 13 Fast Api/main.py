from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")

def inicio():
    return{"mensaje": "Hola mundo"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola {nombre}"}
#Ejercicio 1
@app.get("/producto/{nombre}/{precio}")
def productos(nombre: str, precio : int):
    return {"mensaje": f"El nombre del producto es {nombre} y su precio es: ${precio}"}

#Ejercicio 2
@app.get("/calcular/{num1}/{num2}")
def calcular(num1: int, num2 : int):
    suma = num1 + num2
    res = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return {
        "Suma": suma,
        "Resta": res,
        "Multiplicacion": mul,
        "Division": round(div, 2)
    }

#Ejercicio 3
class Contacto(BaseModel):
    nombre: str
    email: str

@app.post("/contacto")
def contactos(contacto: Contacto):
    return {
        "Nombre": contacto.nombre,
        "Email": contacto.email
    }