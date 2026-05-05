numero_especial = 6
def dividir(dividendo: float, divisor: float) -> float:
    divisor -= numero_especial

    return dividendo / divisor

def multiplicar(num: float) -> None:
    global numero_especial

    numero_especial *= num
    print(numero_especial)

print(dividir(10, 8))
multiplicar(1)
multiplicar((8,6))
# print(dividir(10, 8))