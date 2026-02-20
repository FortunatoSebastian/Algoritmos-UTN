lista = []


while True:
    elementos = input("Ingresa numeros para la lista: ")
    
    if elementos.lower() == "salir":
        break
    lista.append(elementos)

print("Lista final: ", lista)