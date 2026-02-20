nombres = ["juan","ana","carlos","belen","fran"]
edades = [54,29,20]
ciudades = ["lima","madrid","mexico"]

combinados = list(zip(nombres, edades, ciudades))

# print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")