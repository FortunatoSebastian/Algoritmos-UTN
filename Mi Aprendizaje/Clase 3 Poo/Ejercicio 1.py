import os
os.system("cls")

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def mostrar(self):
        print(f"El nombre del producto es: {self.nombre} y el precio es: ${self.precio}")

producto1 = Producto("Lata de tomate", 1000)
producto2 = Producto("Arroz de KIlo", 1300)

producto1.mostrar()
producto2.mostrar()

