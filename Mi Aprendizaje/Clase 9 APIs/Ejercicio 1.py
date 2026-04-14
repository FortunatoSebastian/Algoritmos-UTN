# Ejercicio 1 — Fácil:
# Creá una cuenta en OpenWeatherMap, obtené tu API key y hacé un programa que le pida al usuario una ciudad y muestre la temperatura, humedad y descripción del clima.
import requests

API_KEY = "f59ca2002317168cc9dca8f07b0ca8a3"
ciudad = "Buenos Aires"

url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"

respuesta = requests.get(url)
datos = respuesta.json()
print(datos)

# print(f"Ciudad: {datos['name']}")
# print(f"Temperatura: {datos['main']['temp']}°C")
# print(f"Clima: {datos['weather'][0]['description']}")