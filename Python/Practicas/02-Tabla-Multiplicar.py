def tabla_multiplicar():
    numero = int(input("Ingresa un numero: "))
    for i in range(11):
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar()