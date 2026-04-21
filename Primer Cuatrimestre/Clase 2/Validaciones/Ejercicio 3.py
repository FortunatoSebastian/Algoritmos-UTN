import random
clave_secreta = random.randint(1,3)
usuario = ""
while usuario != clave_secreta:
    usuario = int(input("Ingrese un numero del 1 al 10: "))

    if usuario != clave_secreta:
        print("Clave incorrecta")
    else:
        print("Usuario correcto")