import os
os.system("cls")

print("====== Datos Requeridos ======")
print("1. Apellido")
print("2. Edad ")
print("3. Estado Civil")
print("4. Numero de legajo")
print("="*30)



apellido = input("1. Ingrese su Apellido: ")

edad = int(input("2. Ingrese su Edad entre(18 y 90) años: "))
while edad < 18 or edad > 90:
    print("Edad fuera del limite, Reingrese su Edad: ")
    edad = int(input("Reingrese su edad: "))

estado_civil = input("3. Ingrese su Estado Civil [Soltero/a, Casado/a, Divorciado/a, Viudo/a]: ")
# while not estados_civiles:
while estado_civil != "soltero" and estado_civil != "casado" and estado_civil != "divorciado" and estado_civil != "viudo":
    print("Error: Estado civil no reconocido.")
    estado_civil = input("Ingrese nuevamente su Estado Civil: ")

legajo = int(input("4. Ingrese su legajo (Numero de 4 cifras, sin ceros a la iquierda): "))
while legajo < 1000 or legajo > 9999:
    print("Error: El leggajo debe ser un numero de 4 cifras. ingrese nuevamente su legajo")
    legajo = int(input("Reingrese su numero de legajo: "))


print("\n===== Datos Cargados =====")
print("="*30)
print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado Civil: {estado_civil}")
print(f"Legajo: {legajo}")
print("="*30)