nombres = ["juan","ana","carlos","belen","fran"]

for n in nombres:
    numero_letra = nombres.index(n) + 1
    # print("Hola: " + n)
    
    print(f"Nombre {numero_letra}: {n}")

#STARSWITH = COMIENZA CON .....
for nombre in nombres:
    if nombre.startswith('b'):
        print(nombre)

numeros = [1,2,3,4,5]
mi_valor = 0

for x in numeros:
    mi_valor = mi_valor + x

    print(mi_valor)
print("\n")
print(mi_valor)

dic = {"Clave1": "a","Clave2": "b","Clave3": "c"}

for item in dic:
    print(item)