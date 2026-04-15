numero = 1
total = 0

while numero <= 10:
    if numero % 2 == 0:
        total += numero
    numero += 1

print(f"La suma de los números pares del 1 al 10 es: {total}")