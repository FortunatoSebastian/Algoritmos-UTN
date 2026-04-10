import os
os.system("cls")

# Entrada
PRECIO = 800
cantidad_lamparas = int(input("Ingrese cantidad de lamparas: "))
marca = input("Ingrese marca: ")


descuento = 0
descuento_extra = 0
total_sin_descuento = PRECIO * cantidad_lamparas
marca_lower = marca.lower()

# Proceso 
if cantidad_lamparas >= 6:
    descuento = total_sin_descuento * 0.50
elif cantidad_lamparas == 5 and marca_lower == "argentinaluz":
    descuento = total_sin_descuento * 0.40
elif cantidad_lamparas == 5:
    descuento = total_sin_descuento * 0.30
elif cantidad_lamparas == 4 and (marca_lower == "argentinaluz" or marca_lower == "felipelamparas"):
    descuento = total_sin_descuento * 0.25
elif cantidad_lamparas == 4:
    descuento = total_sin_descuento * 0.20
elif cantidad_lamparas == 3 and marca_lower == "argentinaluz":
    descuento = total_sin_descuento * 0.15
elif cantidad_lamparas == 3 and marca_lower == "felipelamparas":
    descuento = total_sin_descuento * 0.10
elif cantidad_lamparas == 3:
    descuento = total_sin_descuento * 0.05


total_con_descuento = total_sin_descuento - descuento

if total_con_descuento > 4000:
    descuento_extra = total_con_descuento * 0.05

total_a_pagar = total_con_descuento - descuento_extra

# Salida
print(f"Marca: {marca}")
print(f"Cantidad de lámparas: {cantidad_lamparas}")
print(f"Total sin descuento: ${total_sin_descuento:.2f}")
if descuento > 0:
    print(f"Descuento aplicado: ${descuento:.2f}")
if descuento_extra > 0:
    print(f"Descuento adicional (5%): ${descuento_extra:.2f}")
print(f"Total a pagar: ${total_a_pagar:.2f}")