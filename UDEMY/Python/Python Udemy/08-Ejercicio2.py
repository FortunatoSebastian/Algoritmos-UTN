nombre = input("Ingrese su nombre: ")    
ventas = float(input("Ingrese la cantidad de ventas hechas: "))

ventas = int(ventas)

calculo = ventas * 13 / 100
calculo = round(calculo,2)

print("-----------------------------------")
print(f"{nombre} el valor total recibido por comision de las ventas hechas es: ${calculo}")