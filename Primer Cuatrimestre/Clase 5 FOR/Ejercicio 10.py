numero = int(input("Ingrese un numero: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:
    for n in range(2, numero):
        if numero % n == 0:
            es_primo = False
            print(n)

if es_primo:
    print("Es primo")
else:
    print("No es primo")