import os
os.system("cls")

empleados = 0

masculino_iot_ia = 0
contador_no_ia = 0

mayor_edad_masculino = 0
nombre_mayor = ""
tecnologia_mayor = ""

while empleados < 3:
    print(f"\nEmpleado {empleados + 1}")
    
    nombre = input("Ingrese su nombre: ")


    while True:
        edad = int(input("Ingrese su edad (18 o más): "))
        if edad >= 18:
            break
        else:
            print("Error, debe ser mayor de edad.")


    while True:
        genero = input("Genero (masculino/femenino/otro): ").lower()
        if genero in ["masculino", "femenino", "otro"]:
            break
        else:
            print("Error en género.")


    while True:
        tecnologia = input("Tecnologia (ia/rv/iot): ").lower()
        if tecnologia in ["ia", "rv", "iot"]:
            break
        else:
            print("Error en tecnologia.")

    print("="*30)


    if genero == "masculino" and 25 <= edad <= 50 and tecnologia in ["ia", "iot"]:
        masculino_iot_ia += 1


    if genero != "femenino" and 33 <= edad <= 40 and tecnologia != "ia":
        contador_no_ia += 1

    if genero == "masculino":
        if edad > mayor_edad_masculino:
            mayor_edad_masculino = edad
            nombre_mayor = nombre
            tecnologia_mayor = tecnologia

    empleados += 1

# RESULTADOS
porcentaje = (contador_no_ia / empleados) * 100

print("\n" + "="*50)
print(f"Masculinos (25-50) que votaron IA o IOT: {masculino_iot_ia}")

print(f"Porcentaje que NO votaron IA: {porcentaje:.2f}%")

if nombre_mayor != "":
    print(f"Masculino de mayor edad: {nombre_mayor} ({mayor_edad_masculino} años) - Votó: {tecnologia_mayor}")
else:
    print("No se ingresaron empleados masculinos.")

print("="*50)