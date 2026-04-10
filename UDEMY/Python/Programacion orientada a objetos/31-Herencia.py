class Animal:

    def __init__(self, edad, color, nombre):
        self.edad = edad
        self.color = color
        self.nombre = nombre

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

class Elefante(Animal):
    pass


piolin = Pajaro(2, "Amarillo", "gorrion")
elefante = Elefante(10, "Gris claro", "Dumbo")

print(piolin.edad)
print(f"{elefante.nombre} tiene {elefante.edad} años y es de color {elefante.color}")
