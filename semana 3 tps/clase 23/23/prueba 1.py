tipo_cliente = input("ingrese el tipo de cliente: |regular/premium/nuevo| ")
monto = float(input("ingrese el monto total de la compra: "))

puntos = 0

match tipo_cliente:
    case "regular":
        if monto > 10000:
            puntos = 10
    case "premium":
        puntos = 20
    case "nuevo":
        if monto > 5000:
            puntos = 5

print(f"Usted recibe {puntos} puntos")