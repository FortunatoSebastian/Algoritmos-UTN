usuarios = [
    ["Chanchito", 4],
    ["Perrito", 8],
    ["Pajarito", 2],
    ["Vaquita", 1],
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

#BUSQUEDA DE LISTA CON FOR - MAP 
# nombres = [usuario[0] for usuario in usuarios]

#FILTRAR-FILTER
# nombres = [usuario for usuario in usuarios if usuario [1] > 2]

#FILTRAR Y TRANSFORMAR
# nombres = [usuario[0] for usuario in usuarios if usuario [1] > 2]

#MAP
# nombres = list(map(lambda usuario: usuario[0], usuarios))

#FILTER
nombres = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(nombres)