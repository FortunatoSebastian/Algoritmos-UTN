import os
os.system("cls")

# Ejercicio 2 — Carrito de compras
# Creá una clase Carrito con un atributo productos que arranque como una lista vacía. Agregá tres métodos:

# agregar(nombre, precio) que agregue un diccionario con esos datos a la lista
# mostrar() que imprima todos los productos del carrito
# total() que imprima la suma de todos los precios

# Probalo agregando 3 productos y mostrando el carrito y el total.

class Carrito:
    def __init__(self):
        self.producto = []
    
    def agregar(self, nombre, precio):
        self.producto.append({"nombre": nombre, "precio": precio})

    def mostrar(self):
        for producto in self.producto:
            print("="*50)
            print(f"""Nombre: {producto["nombre"]} \nPrecio: ${producto["precio"]}""")
        print("="*50)
        
    def total(self):
        total = 0
        for producto in self.producto:
            total += producto["precio"]
        print(f"El total es: ${total}")

producto = Carrito()

producto.agregar("Lata de tomate", 1000)
producto.agregar("Arroz de kilo", 2000)
producto.agregar("Galletita de agua", 1800)

producto.mostrar()

producto.total()