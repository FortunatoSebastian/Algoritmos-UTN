
def mensajes(mensaje: str, mensaje_error: str, ) -> tuple:
    return mensaje, mensaje_error

def minimo_maximo(minimo:int, maximo:int) -> int:
    return minimo, maximo

def main():
    exito, error = mensajes("Edad permitida es +18", "Edad no permitida")
    minimo, maximo = minimo_maximo(minimo=17, maximo=60)
    while True:
        edad = int(input("Ingrese su edad: "))

        if minimo <= edad <= maximo:
            print(exito)
        else:
            print(error)
        
main()