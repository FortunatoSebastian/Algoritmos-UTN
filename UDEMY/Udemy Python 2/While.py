import os
os.system("cls")
# numero = 1

# while numero < 100:
#     print(numero)
#     numero += 1

comando = ""

# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)
def tabla_de_multiplicar():
    print("Tabla de multiplicar")
    numero = int(input("Ingrese un numero para multiplicar"))

    for n in range(11):
        print(f"{numero} x {n} = {numero * n}")
tabla_de_multiplicar()