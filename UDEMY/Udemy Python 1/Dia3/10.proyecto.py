import os
os.system("cls")
# texto = "Solo una decisión puede cambiar el curso de todo. Una vez descarriado, no hay vuelta atrás. Y cuando te canses de tus torpes avances, vas a susurrar: se suponía que esto no debía acabar así."
texto = "hola como estas python"

letras = []

letras.append(input("ingresa la primera letra: "))
letras.append(input("ingresa la primera letra: "))
letras.append(input("ingresa la primera letra: "))

#PRIMERA PARTE
#---------------------------------------------------------------------
os.system("cls")
print("Cantidad de letras que se repiten: ")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"La letra '{letras[0]}' aparece {cantidad_letras1} vez/veces")
print(f"La letra '{letras[1]}' aparece {cantidad_letras2} vez/veces")
print(f"La letra '{letras[2]}' aparece {cantidad_letras3} vez/veces")
print("\n")

#---------------------------------------------------------------------
#SEGUNDA PARTE

palabras = texto.split()
# cantidad_palabras = len(palabras)

# print("Cantidad de palabras: ", cantidad_palabras)

print(f"Hemos encontrado {len(palabras)} palabras en tu texto")
print("\n")
#---------------------------------------------------------------------
#TERCERA PARTE
print("Primera y ultima letras: ")

primera_letra = texto[0].upper()
ultima_letra = texto[-1].upper()

print(f"La primera letra del texto es: {primera_letra}\ny la ultima letra del texto es: {ultima_letra}")
print("\n")
#---------------------------------------------------------------------
#CUARTA PARTE

print("Mostrar el texto en reverza: ")

texto_reverso = texto[::-1]

print(texto_reverso)
print("\n")
#---------------------------------------------------------------------
#QUINTA PARTE

x = "python"

if x in texto:
    print("SI, la palabra Python esta en el texto.")
else:
    print("NO, la palabra Python no esta en el texto.")