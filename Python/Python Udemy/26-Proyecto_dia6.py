import os
from pathlib import Path
from os import system

mi_ruta = Path("C:\\Users\\Damia\\Desktop\\Recetas")


def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


def inicio():
    system("cls")
    print("*" * 50)
    print("*" * 5 ,"Bienvenido al administrador de recetas","*" * 5)
    print("*" * 50)
    print("\n")
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = "X"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - salir del programa''')
        eleccion_menu = input()
    return(eleccion_menu)

def mostrar_categorias(ruta):
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador +=1

    return lista_categorias


def elegir_categoria(lista):
    eleccion_correcta = "x"



inicio()

menu = 0

if menu == 1:
    mis_categorias = mostrar_categorias(mi_ruta)
    # elegir Categoria
    # mostrar recetas
    # elegir reetas
    # leer recetas
    # volver inicio
    pass
elif menu == 2:
    mis_categorias = mostrar_categorias(mi_ruta)
    # elegir categoria
    # crear reeta nueva
    # volver inicio
    pass
elif menu == 3:
    # crear categoria
    # volver inicio
    pass
elif menu == 4:
    mis_categorias = mostrar_categorias(mi_ruta)
    # elegir categorias
    # mostrar recetas
    # elegir recetas
    # eliminar recetas
    # volver inicio
    pass
elif menu == 5:
    mis_categorias = mostrar_categorias(mi_ruta)
    # elegir categorias
    # eliminar categoria
    # volver inicio
    pass
elif menu == 6:
    # finalizar programa
    pass