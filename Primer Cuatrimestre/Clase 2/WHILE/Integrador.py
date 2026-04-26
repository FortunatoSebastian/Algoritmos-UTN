suma_negativos = 0
suma_positivos = 0
contador_negativos = 0
contador_positivos = 0
mayor_positivo = None
total_numeros = 0

continuar = "si"

while continuar == "si":
    numero = int(input("Ingrese un número: "))
    total_numeros += 1

    if numero < 0:
        suma_negativos += numero
        contador_negativos += 1
    elif numero > 0:
        suma_positivos += numero
        contador_positivos += 1

        if mayor_positivo is None or numero > mayor_positivo:
            mayor_positivo = numero

    continuar = input("¿Querés seguir ingresando números? (si/no): ")


print(f"Suma de negativos: {suma_negativos}")
print(f"Suma de positivos: {suma_positivos}")
print(f"Cantidad de negativos: {contador_negativos}")

if contador_positivos > 0:
    promedio_positivos = suma_positivos / contador_positivos
    print(f"Promedio de positivos: {promedio_positivos}")
else:
    print("No se ingresaron números positivos")

if mayor_positivo is not None:
    print(f"Mayor número positivo: {mayor_positivo}")
else:
    print("No se ingresaron números positivos")

if total_numeros > 0:
    porcentaje_negativos = (contador_negativos * 100) / total_numeros
    print(f"Porcentaje de negativos: {porcentaje_negativos}%")