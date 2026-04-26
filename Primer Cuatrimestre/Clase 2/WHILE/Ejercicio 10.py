suma = 0
contador = 0

while contador < 10:
    numero = int(input("Ingrese un número: "))
    suma += numero
    contador += 1

    if contador >= 5:
        seguir = input("¿Desea ingresar otro número? (s/n): ")
        if seguir.lower() = "n":
            break

promedio = suma / contador

print(f"Suma total: {suma}")
print(f"Promedio: {promedio}")