mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]

#LEN CUENTA CUANTOS ITEMS HAY EN LA LISTA
resultado = len(mi_lista)

#CORCHETE TE MARCA QUE ITEM HAY EN EL NUMERO MARCADO
resultado2 = mi_lista[0]
resultado3 = mi_lista[0:2]

resultado4 = mi_lista + mi_lista2

print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)

#APPEND AGREGA UN ITEM A LA LISTA
mi_lista2.append("g")

#POP ELIMINA UN ITEM EN LA LISTA
mi_lista.pop()

print(mi_lista2)


lista = ["g","c","b","a","s"]
lista2 = ["g","c","b","a","s"]
#SORT ORDENA LA LISTA
lista.sort()
#REVERSE LEE LA LISTA DESDE EL ULTIMO ITEM
lista2.reverse()

print(lista)
print(lista2)