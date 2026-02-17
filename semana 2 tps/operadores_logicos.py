edad = int(input("Ingrese su edad: "))
categoria = input("Ingrese su categoria: (a, b, c, d, e, f, g): ")
edad_minima = 21

if edad >= edad_minima and (categoria == "D" or categoria == "d"):
    print("Puede conducir ambulancias")
else:
    print("No puede conducir ambulancias")

