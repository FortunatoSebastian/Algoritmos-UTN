try:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))

    div = num1 / num2
    print(div)
except ValueError:
    print("Error: Tenes que ingresar un numero")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
