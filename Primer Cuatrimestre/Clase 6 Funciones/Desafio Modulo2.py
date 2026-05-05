def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> str | None:
    for i in range(reintentos + 1):
        cadena = input(mensaje)
        
        if len(cadena) <= longitud:
            return cadena
        
        if i < reintentos:
            print(f"{mensaje_error} (Máximo {longitud} caracteres)")
        
    return None

nombre = get_string("Ingrese su nombre: ", "Nombre demasiado largo.", 10, 2)

if nombre:
    print(f"Nombre ingresado es: {nombre}")
else:
    print("No se pudo obtener un nombre valido.")