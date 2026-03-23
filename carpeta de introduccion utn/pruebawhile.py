import os 
os.system("cls")
# moneda = 5

# while moneda > 0:
#     print(f"Tienes {moneda} de monedas.")
#     moneda -= 1
#     if moneda == 0:
#         print("Te quedaste sin monedas")

# lista = [1,2,3,4,7,11,40,50]
# for n in lista:
#     print(n)

numeros = []
for x in range(5):
    numero = int(input("ingrese 5 numeros: "))
    numeros.append(numero)
    print(f"los números son: {numeros}")