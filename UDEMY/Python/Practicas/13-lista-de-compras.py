lista = []

while True:
    elementos = input("Ingrese el nombre del producto que quiera agregar a la lista: ")

    if elementos.lower() == "fin":
        break
    lista.append(elementos)
print("Los productos para comprar son: ", lista)