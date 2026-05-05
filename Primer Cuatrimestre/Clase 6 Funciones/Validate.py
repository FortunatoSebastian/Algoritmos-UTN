def validate_number(numero: int | float, minimo: int | float, maximo: int | float) -> bool:
    return minimo <= numero <= maximo

def validate_length(cadena: str, longitud: int) -> bool:
    return len(cadena) <= longitud