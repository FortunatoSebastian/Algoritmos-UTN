suma = 0
contador = 0

while contador < 5:
    numero = int(input("Ingrese un número: "))
    suma += numero
    contador += 1

promedio = suma / contador

print(f"Suma total: {suma}")
print(f"Promedio: {promedio}")