import os
os.system("cls")
#Entrada
PRECIO = 1800
cantidad_lamparas = int(input("Ingrese cantidad de lamparas: "))
marca = input("Ingrese marca: ").lower()
print("\n")
descuento_extra = 0
total_sin_descuento = PRECIO * cantidad_lamparas

#Proceso
if cantidad_lamparas >= 6:
    descuento = 0.50
elif cantidad_lamparas == 5:
    if marca == "ArgentinaLuz":
        descuento = 0.40
    else:
        descuento = 0.30
elif cantidad_lamparas == 4:
    if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
        descuento = 0.25
    else:
        descuento = 0.20
elif cantidad_lamparas == 3:
    if marca == "ArgentinaLuz":
        descuento = 0.15
    elif marca == "FelipeLamparas":
        descuento = 0.10
    else:
        descuento = 0.05
elif cantidad_lamparas < 3:
    descuento = 0.0

descuen_aplicar = total_sin_descuento * descuento

descuento = total_sin_descuento * descuento

total_con_descuento = total_sin_descuento - descuento

if total_con_descuento > 4000:
    descuento_extra = total_con_descuento * 0.05

total_a_pagar = total_con_descuento - descuento_extra

print("-" * 50)
print(f"Cantidad de unidades compradas: {cantidad_lamparas}")
print(f"Nombre del producto: {marca}")
print("-" * 50)
print(f"Precio Total: ${total_sin_descuento}")
print(f"Descuento aplicado: ${descuento}")
if descuento > 0:
    print(f"Descuento extra aplicado: ${descuento_extra}")
print(f"Precio Final: ${total_a_pagar}")
print("-" * 50)

# datadriven