#ENTRADA
lado_keops = float(input("Ingrese el lado de la piramide de keops: "))
altura_keops = float(input("Ingrese la altura de la piramide de keops: "))
#PROCESO
# altura_inclinada_keops = ((altura_keops**2) + (lado_keops**2)/4)**0.5
# area_keops = lado_keops**2 + 4 * (lado_keops*altura_inclinada_keops)/2

area_keops = lado_keops * (lado_keops + (4*(altura_keops**2) + lado_keops**2)**0.5)

#SALIDA
print(f"El Area de Keops {area_keops}")