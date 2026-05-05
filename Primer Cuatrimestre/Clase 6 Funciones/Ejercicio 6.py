# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar

def par_impar():
    numero = int(input("Ingrese un numero para saber si es par o impar: "))

    if numero % 2 == 0:
        print(f"{numero} es numero |PAR|")
    else:
        print(f"{numero} es numero |IMPAR|")

par_impar()