mascota = "perro"

if mascota == "gato":
    print("tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
else:
    print("no se que anima tienes")


edad = 20
calificacion = 8

if edad < 18:
    print("eres menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("No aprobrado")
else:
    print("eres adulto")