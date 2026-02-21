x = int(input("Coloca un numero entero: "))

if x == 0:
    resultado = "neutro"
elif x > 0:
    resultado = "positivo"
else:
    resultado = "negativo"

print(f"{x} es {resultado}")