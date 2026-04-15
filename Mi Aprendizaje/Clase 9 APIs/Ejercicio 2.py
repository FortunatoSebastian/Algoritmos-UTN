import requests
import os
os.system("cls")


# ciudad = input("Ingresa una Ciudad: ")
ciudad = "Buenos Aires"
API_KEY = "My key"

url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"

respuesta = requests.get(url)
datos = respuesta.json()

print(datos)

print("="*50)
if respuesta.status_code == 200:
    print(f"Ciudad: {datos['name']}")
    print(f"Temperatura Actual: {datos['main']['temp']}°C")
    print(f"Temperatura Minima: {datos['main']['temp_min']}°C")
    print(f"Temperatura Maxima: {datos['main']['temp_max']}°C")
    print(f"Clima: {datos['weather'][0]['description']}")
    print(f"Viento: {datos['wind']['speed']} m/s")
    print(f"Dirección: {datos['wind']['deg']}°")
    print(f"Ráfagas: {datos['wind'].get('gust', 'No disponible')}")
else:
    print("Error:", datos.get("message", "No se pudo obtener el clima"))