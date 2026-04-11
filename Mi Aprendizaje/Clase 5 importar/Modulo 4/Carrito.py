class Carrito:
    def __init__(self):
        self.producto = []

    def agregar(self, nombre, precio):
        self.producto.append({"nombre": nombre, "precio": precio})

    def mostrar(self):
        for producto in self.producto:
            print(f"El Producto: {producto["nombre"]}, Vale: ${producto["precio"]}")