nombre = input("Ingrese su nombre: ")

with open("nombres.txt", "a") as archivo:
    archivo.write(f"Nombres: {nombre}\n")