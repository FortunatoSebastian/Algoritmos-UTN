texto = input("Ingresa algun texto: ").lower()
letras = []
print("\n1. Ingrese algunas letras para saber cuantas veces aparece en el texto.")
letras.append(input(f"\n Ingrese la primera letra: ").lower())
letras.append(input(f" Ingrese la segunda letra: ").lower())
letras.append(input(f" Ingrese la tercera letra: ").lower())


print("\n cantidad de letras")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"la letra {letras[0]} se repitio {cantidad_letras1} veces")
print(f"la letra {letras[1]} se repitio {cantidad_letras2} veces")
print(f"la letra {letras[2]} se repitio {cantidad_letras3} veces")


palabras = texto.split()
print(f"\n2. Cuantas palabras hay en el texto.")
print(f"    Total de palabras: {len(palabras)}")


primero_y_ultima = [l for l in texto if l.isalpha()]
if primero_y_ultima:
    print(f"\n3. Cual es la primera letra y la ultima letra del texto")
    print(f"    primera letra: {primero_y_ultima[0]}")
    print(f"    ultima letra: {primero_y_ultima[-1]}")
else:
    print("\n3. No hay letras en el texto")


palabra_inverso = palabras[::-1]
print("\n4. palabra en orden inverso: ")
print(  " ".join(palabra_inverso))

print("\n5. ¿aparece la palabra python?")
if 'python' in palabras:
    print(" si, aparece")
else:
    print(" no, no aparece.")
