def mensajes(mensaje: str, mensaje_error: str) -> tuple:
    return mensaje, mensaje_error

def largo(longitud: int) -> int:
    return longitud

def get_string(longitud: int) -> str | None:
    exito, error = mensajes("Cadena válida", f"Error: la cadena debe tener exactamente {longitud} caracteres")
    limite = largo(longitud)

    while True:
        cadena = input(f"Ingrese una cadena de {limite} caracteres: ")

        if len(cadena) == limite:
            print(exito)
            return cadena
        else:
            print(error)

def main():
    resultado = get_string(5)
    print(f"Cadena ingresada: {resultado}")

main()