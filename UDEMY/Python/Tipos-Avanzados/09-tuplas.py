numeros = (1, 2, 3) + (4, 5, 6)

print(numeros)

punto = tuple([1, 2])
print(punto)
menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)
#Tuplas no se pueden modificar
#Solo las listas se pueden modificar

listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito feliz"
print(listaNumeros)