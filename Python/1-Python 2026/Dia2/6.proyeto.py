nombre = input("Ingrese su nombre: ")
ventas = input("Ingrese su cantidad de ventas: ")

ventas = int(ventas)
comision = ventas * 13 / 100

print(f"Hola {nombre}, tu comision de este mes es ${comision}")