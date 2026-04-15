import os 
os.system("cls")

acumulador = 0
suma_total = 0
numero = 0

while True:
    numero = int(input(f"{acumulador + 1}. Ingrese un numero: "))
    
    if numero == -1:
        break
    suma_total += numero
    acumulador += 1

promedio = suma_total / acumulador

print(f"La suma total es: {suma_total}")
print(f"El promedio es: {promedio}")