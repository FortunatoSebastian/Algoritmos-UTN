import os 
os.system("cls")

maximo = None
minimo = None
contador = 0

while contador < 10:
    numero = int(input(f"{contador + 1}. Ingrese numeros: "))

    if contador == 0:
        maximo = numero
        minimo = numero
    else:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    
    contador = contador + 1

print(f"maximo: {maximo}")
print(f"minimo: {minimo}")