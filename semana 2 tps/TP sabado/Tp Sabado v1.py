import os
os.system("cls")


#Entrada
PRECIO = 1800
cantidad_lamparas = int(input("Ingrese cantidad de lamparas: "))
marca = input("Ingrese marca: ")

print("\n")
descuento_extra = 0
total_sin_descuento = PRECIO * cantidad_lamparas

#Proceso
if cantidad_lamparas >= 6:
    descuento = total_sin_descuento * 0.50
elif cantidad_lamparas == 5 and marca == "ArgentinaLuz".lower():
    descuento = total_sin_descuento * 0.40
elif cantidad_lamparas == 5:
    descuento = total_sin_descuento * 0.3
elif cantidad_lamparas == 4 and (marca == "ArgentinaLuz".lower() or marca == "FelipeLamparas".lower()):
    descuento = total_sin_descuento * 0.25
elif cantidad_lamparas == 4:
    descuento = total_sin_descuento * 0.2
elif cantidad_lamparas == 3 and marca == "ArgentinaLuz".lower():
    descuento = total_sin_descuento * 0.15
elif cantidad_lamparas == 3 and marca == "FelipeLamparas".lower():
        descuento = total_sin_descuento * 0.10
elif cantidad_lamparas == 3:
        descuento = total_sin_descuento * 0.05

# descuento = total_sin_descuento * porcentaje_descuento
total_con_descuento = total_sin_descuento - descuento
if total_con_descuento > 4000:
    descuento_extra = total_con_descuento * 0.05
total_a_pagar = total_con_descuento - descuento_extra
print(total_con_descuento)

#SALIDA
