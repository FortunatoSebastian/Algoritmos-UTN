# serie = input("Ingresa un numero: ")

# match serie:
#     case "1":
#         print("Samsung")
#     case "2":
#         print("Nokia")
#     case "3":
#         print("Motorola")
#     case _:
#         print("No existe este producto")

cliente = {"nombre": "federico",
           "edad":45,
           "ocupacion": "instructor"}

pelicula = {"titulo": "matrix",
            "ficha_tecnica": {"protagonista": "keanu reeves",
                              "director": "lana y lilly wachowski"}}

elementos = [cliente,pelicula, "libro"]

for e in elementos:
    match e:
        case{"nombre": nombre,
             "edad": edad,
             "ocupacion": ocupacion}:
            print("es un cliente")
            print(nombre, edad, ocupacion)
        case{"titulo": titulo,
             "ficha_tecnica": {"protagonista": protagonista,
                               "director": director}}:
            print("es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("no se que es esto")