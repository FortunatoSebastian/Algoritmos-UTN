import os
import requests
import csv
from datetime import datetime
os.system("cls")

ciudad = input("Ingresa una ciudad: ")
API_KEY = "My key"

url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"

respuesta = requests.get(url)
datos = respuesta.json()

if respuesta.status_code == 200:
    nombre = datos['name']
    temp = datos['main']['temp']
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Ciudad: {nombre}")
    print(f"Temperatura: {temp}°C")

    # 🔽 Guardar en CSV
    with open("historial_clima.csv", "a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre, temp, fecha])

else:
    print("Error:", datos.get("message", "No se pudo obtener datos"))