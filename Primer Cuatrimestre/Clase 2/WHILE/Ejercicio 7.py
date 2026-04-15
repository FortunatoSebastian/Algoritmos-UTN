# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

import os 
os.system("cls")

suma = 0
producto = 1
acumulador = 0
suma_total = 0
numero = 0


while True:
    numero = int(input(f"{acumulador + 1}. Ingrese numeros: "))
    if numero == -1:
        break

    if numero > 0:
        suma = suma + numero
    elif numero < 0:
        producto = producto * numero

print(f"La suma de los positivos es: {suma}")
print(f"Producto de negativos: {producto}")