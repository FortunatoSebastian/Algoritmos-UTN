total = float(input("Ingrese un valor: "))

if total > 1000:
    porcentaje = 20
elif total >= 500:  # Ya sabemos que total <= 1000 por el if anterior
    porcentaje = 10
else:
    porcentaje = 0

descuento = total * porcentaje / 100

print(f"Total de la compra: ${total:.2f} | Descuento del {porcentaje}%: ${descuento:.2f}")