class Enemigo1:
    def __init__(self, vida, color, nombre):
        self.vida = vida
        self.color = color
        self.nombre = nombre


class Zombie(Enemigo1):
    pass

zombie1 = Zombie(100, "verde", "carlos el zombie")

print(f"{zombie1.nombre} tiene {zombie1.vida} puntos de vida y es de color {zombie1.color}")