# numeros = [2, 3, 6, 78, 10, 50, 20]

# # numeros.sort(reverse=True)
# numeros2 = sorted(numeros)

# print(numeros)
# print(numeros2)

usuario = [
    ["Chanchito", 4],
    ["Perrito", 8],
    ["Pajarito", 3],
    ["Vaquita", 1],
]
# def ordena(elemento):
#     return elemento[1]

usuario.sort(key=lambda el: el[1], reverse=True) #La funcion de LAMBDA es igual a def pero de forma anonima, solo usar si no tengo otros def en mi codigo o que los def solo se usen 1 vez
print(usuario)