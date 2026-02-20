nombres = ['ana','hugo','valeria']
edades = [65,20,30]
paises = ['argentina','mexico','chile']

combinados = list(zip(nombres, edades,paises))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")



