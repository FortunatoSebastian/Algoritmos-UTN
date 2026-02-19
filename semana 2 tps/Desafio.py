# Crear un programa que muestre en la consola 
# 10 repeticiones con números ASCENDENTE desde el 1 al 10

# contador = 0
# contador = contador +1
# print(contador)
# contador = contador +1
# print(contador)
# contador = contador +1
# print(contador)
# contador = contador +1
# print(contador)
# contador = contador +1
# print(contador)
# contador = contador +1
# print(contador)
# contador = contador +1
# print(contador)
# contador = contador +1
# print(contador)
# contador = contador +1
# print(contador)
# contador = contador +1
# print(contador)

# for i in range(1, 11):
#     print(i)
#while for vectores = listas 
# fibonacci 
import os
os.system("cls")

a = 0
b = 1
lista = []
for i in range(32):

    a,b = (b, a+b)
    if a % 2 == 0:
        lista.append(a)
        print(a)
        
    #   print("El valor actual de a y es PAR:", a)
    # else:
    #   print("El valor actual de a y es IMPAR:", a)