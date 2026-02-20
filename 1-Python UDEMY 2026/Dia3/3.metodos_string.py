import os
os.system("cls")
texto = "Este es el texto de federico"

resultado = texto.upper()
resultado2 = texto.lower()
resultado3 = texto.split()
resultado4 = texto.find("s")
resultado5 = texto.replace("federico","messi")

print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)



a = "aprender"
b = "python"
c = "es"
d = "genial"
e = "_".join([a,b,c,d])
print(e)