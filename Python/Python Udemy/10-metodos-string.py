texto = "Hola pedazo de gato"
resultado = texto.upper()#MAYUSCULA
resultado2 = texto.lower()#MINUSCULA
resultado3 = texto.split()#SEPARA EN LISTA Y PUEDE QUITAR LETRAS DE LA LISTA
resultado4 = texto.find("g")#BUSCA UN CARACTER DENTRO DE UN STING
resultado5 = texto.replace("gato","puto")#REMPLAZA TEXTO O LETRAS


print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)

a = "aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)