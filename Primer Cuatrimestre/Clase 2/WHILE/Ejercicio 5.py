import os 
os.system("cls")

cantidad_numeros = 5
suma_total = 0
contador = 0

while contador < cantidad_numeros:
    numeros = float(input(f"Ingrese un numero {contador + 1}: "))

    suma_total += numeros

    contador += 1

promedio = cantidad_numeros / numeros

print(f"La suma total es: {suma_total}")
print(f"El promedio es: {promedio}")