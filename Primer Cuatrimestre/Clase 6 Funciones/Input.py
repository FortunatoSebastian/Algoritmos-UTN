from Validate import validate_number, validate_length

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    for i in range(reintentos + 1):
        respuesta = input(mensaje)
        
        if respuesta.isdigit():
            numero = int(respuesta)
            if validate_number(numero, minimo, maximo):
                return numero
        
        if i < reintentos:
            print(mensaje_error)
            
    return None

def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int) -> str | None:
    for i in range(reintentos + 1):
        cadena = input(mensaje)
        
        if validate_length(cadena, longitud):
            return cadena
            
        if i < reintentos:
            print(mensaje_error)
            
    return None