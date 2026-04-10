from pathlib import Path, PureWindowsPath
# from os import system

carpeta = Path("C:/Users/Damia/Desktop/recetas/Carnes/asado.txt")

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)

print(carpeta.stem) #nombre del archivo sin que formato es

# print(carpeta.read_text()) # lee el contenido del archivo

# print(carpeta.name) # nombre del archivo + cual formato es

# print(carpeta.suffix) # muestra que formato esta hecho el archivo




# system("cls")
# if not carpeta.exists(): 
#     print("Este archivo no existe")
# else:
#     print("Genial, existe")