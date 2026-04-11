import productos
import utils

producto1 = productos.Producto("Lata de tomate", 1500)
producto2 = productos.Producto("Galletitas", 2000)
producto3 = productos.Producto("Fiambre", 3000)

utils.limpiar_pantalla()
# utils.separador()
# producto1.mostrar()
# utils.separador()
# producto2.mostrar()
# utils.separador()
# producto3.mostrar()
# utils.separador()

productos_lista = [producto1, producto2, producto3]

for p in productos_lista:
    utils.separador()
    p.mostrar()
utils.separador()