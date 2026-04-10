num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))

operacion = input("introduce una operacion \n Suma '+' \n Resta '-' \n Multiplicacion '*' \n Division '/' ")

match operacion:
    case "+":
        res = num1+num2
    case "-":
        res = num1-num2
    case "*":
        res = num1*num2
    case "/":
        res = num1/num2

print(f"El resultado de {num1} {operacion} {num2} = {res}")