import os
os.system("cls")
# Ejercicio 1 — Sistema de empleados
# Creá una clase Empleado con atributos nombre, puesto y sueldo. Agregá dos métodos:

# mostrar() que imprima los tres datos
# aumentar_sueldo(porcentaje) que le sume al sueldo el porcentaje indicado

# Probala creando 2 empleados, mostrálos, aplicales un aumento distinto a cada uno y mostrálos de nuevo.

class Empleado:
    def __init__(self, nombre, puesto, sueldo):
        self.nombre = nombre
        self.puesto = puesto
        self.sueldo = sueldo
    
    def mostrar(self):
        print(self.nombre)
        print(self.puesto)
        print(self.sueldo)
    
    def aumentar_sueldo(self, porcentaje):
        self.sueldo = self.sueldo + (self.sueldo * porcentaje / 100)

empleado1 = Empleado("Sebastian", "Programador", 2000000)
empleado2 = Empleado("Ezequiel", "Ejecutivo", 1500000)
print("=" * 50)
print(f"""
    Datos de los Empleados \n
    Nombre: {empleado1.nombre} \n
    Puesto: {empleado1.puesto} \n
    Sueldo: ${empleado1.sueldo}
    

""")
print("=" * 50)
print(f"""
    Datos de los Empleados \n
    Nombre: {empleado2.nombre} \n
    Puesto: {empleado2.puesto} \n
    Sueldo: ${empleado2.sueldo}

""")

empleado1.aumentar_sueldo(12)
empleado2.aumentar_sueldo(50)

print("=" * 50)
print(f"""
    Datos de los Empleados \n
    Nombre: {empleado1.nombre} \n
    Puesto: {empleado1.puesto} \n
    Sueldo: ${empleado1.sueldo}
    

""")
print("=" * 50)
print(f"""
    Datos de los Empleados \n
    Nombre: {empleado2.nombre} \n
    Puesto: {empleado2.puesto} \n
    Sueldo: ${empleado2.sueldo}

""")