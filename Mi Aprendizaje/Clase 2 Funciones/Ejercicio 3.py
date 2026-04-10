def crear_perfil(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

crear_perfil(nombre="Sebastian", edad="23")
crear_perfil(nombre="Damian", edad="28", ciudad="Lomas de Zamora", carrera="Analista en Sistemas")