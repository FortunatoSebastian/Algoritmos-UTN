import math

def calcular_circulo(radio):
    area = math.pi * radio**2
    circunferencia = 2 * math.pi * radio
    print(area)
    print(circunferencia)


calcular_circulo(20)