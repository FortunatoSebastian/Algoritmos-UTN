import os
from Carrito import Carrito
os.system("cls")

mi_carrito = Carrito()

mi_carrito.agregar("Lata de tomate", 1000)
mi_carrito.agregar("Arroz de kilo", 2200)
mi_carrito.agregar("Queso rallado", 1400)

mi_carrito.mostrar()