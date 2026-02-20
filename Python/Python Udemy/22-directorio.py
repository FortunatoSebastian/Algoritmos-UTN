import os

# with open("C:\\Users\\Damia\\Desktop\\carpeta2\\ejemplo2.txt","r",encoding="UTF-8") as archivo:
#     print(archivo.read())




#Crea una carpeta dentro del directorio seleccionado---------------
ruta = os.makedirs("C:\\Users\\Damia\\Desktop\\carpeta2\\otra")



#Remueve el archivo o carpeta seleccionada del directorio-----------
# os.rmdir("C:\\Users\\Damia\\Desktop\\carpeta2\\otra") 


#Separa elemento de carpeta de ruta-------------
# ruta = ("C:\\Users\\Damia\\Desktop\\carpeta2\\ejemplo2.txt")
# elemento = os.path.split(ruta)
# print(elemento)