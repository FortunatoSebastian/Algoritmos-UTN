# import os
# os.system("cls")

# while True:
#     print("-" * 50)
#     signo = input("Ingrese un signo para hacer el calculo ( +, -, *, / ): ")
#     num1 = float(input("\nIngrese el primer valor para calcular: "))
#     num2 = float(input("Ingrese el segundo valor para calcular: "))
    
#     match signo.lower():
#         case "+":
#             resultado = num1 + num2
#         case "-":
#             resultado = num1 - num2
#         case "*":
#             resultado = num1 * num2
#         case "/":
#             resultado = num1 / num2
#         case _:
#             print("Signo invalido")
#     print("-" * 50)
#     print(f"El resultado de {num1} {signo} {num2} = {resultado}")

def Menu():
    while True: 
        # os.system("cls")
        print("-" * 50)
        print("1 - Registrarse")
        print("2 - Logearse")
        print("3 - Salida")
        print("-" * 50)
        opciones = input("Ingrese la opcion del MENU que necesite: ")
        match opciones:
            case "1":
                Registro()
            case "2":
                Login()
            case "3":
                print("¡Hasta luego!")
                break
            case _:
                print("Opcion Invalida")

Menu()