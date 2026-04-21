color = input("Ingrese el colo que quieras: ")

while color != "rojo" and color != "azul" and color != "verde":
    print(f"Error: Color {color} no valido")
    color = input("Ingrese nuevamente el color: ")

print(f"Color valido: {color}")