buscar = 3

for numero in range(5):
    print(numero)
    if numero == buscar:
        print(f"Encontramos el numero {buscar}")
        break
else:
    print(f"No encontre el numero")