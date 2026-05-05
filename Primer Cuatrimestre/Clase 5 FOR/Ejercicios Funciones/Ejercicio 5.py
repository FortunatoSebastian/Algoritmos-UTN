suma = 0 
contador = 0

for n in range(10):
    numero = int(input("Ingrese un numero (0 para salir): "))

    if numero == 0:
        break

    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
else:
    print("Numeros invalidos")