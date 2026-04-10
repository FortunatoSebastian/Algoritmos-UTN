# punto = {"x": 25, "y": 50}
# print(punto)
# print(punto["x"])
# print(punto["y"])

# punto["z"] = 45
# print(punto)
# print(punto["z"])

# for valor in punto.items(): #Esta sintaxis me devuelve tuplas
#     print(valor)

usuarios = [
    {"id": 1, "nombre": "chanchito"},
    {"id": 2, "nombre": "pollito"},
    {"id": 3, "nombre": "vaquita"},
    {"id": 3, "nombre": "perrito"},
]

for usuario in usuarios:
    print(usuario["nombre"])