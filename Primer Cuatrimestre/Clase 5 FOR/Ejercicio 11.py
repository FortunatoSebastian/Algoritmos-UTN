numero = int(input("Ingrese un numero: "))

contador_primos = 0

for n in range(1, numero + 1):
    if n > 1:
        es_primo = True

        for i in range(2, n):
            if n % i == 0:
                es_primo = False
                break

        if es_primo:
            print(n)
            contador_primos += 1

print("Cantidad de numeros primos:", contador_primos)