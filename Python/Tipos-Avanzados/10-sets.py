#set significa grupo o conjunto
#set elimina los elementos duplicados


# primer = {1, 1, 2, 2, 3, 4}

#Agrega un elemento al set
# primer.add(5) 

# #Elimina un elemento del set
# primer.remove(1)

# print(primer)

primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

# print(primer | segundo) #Union
# print(primer & segundo) #Interseccion
# print(primer - segundo) #Diferencia
# print(primer ^ segundo) #Diferencia cimetrica

if 5 in segundo:
    print("Hola mundo")
