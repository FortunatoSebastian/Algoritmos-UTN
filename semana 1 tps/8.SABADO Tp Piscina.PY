import os
os.system("cls")
#ENTRADAS
#1-largo, #2-ancho,#3-Profundidad,#4-revestimiento,#5-litros de agua
largo_de_piscina = float(input("Ingrese el largo de la piscina: "))
ancho_piscina = float(input("Ingrese el ancho de la piscina: "))
profundidad_piscina = float(input("Ingrese la profundidad de la piscina: "))
precio_revestimiento = float(input("Ingrese el precio del revestimiento piscina: "))
precio_litro = float(input("Ingrese el precio por litro de agua: "))
#PROCESOS
print(type(largo_de_piscina))
#1
area_base = largo_de_piscina * ancho_piscina
#2
volumen_de_agua = area_base * profundidad_piscina
#3
area_de_pared_grande = (profundidad_piscina * largo_de_piscina) * 2
area_de_pared_chica = (profundidad_piscina * ancho_piscina) * 2
total_revestimiento = area_base + area_de_pared_grande + area_de_pared_chica
#4
litros_agua = volumen_de_agua * 1000
#5
costo_revestimiento = total_revestimiento * precio_revestimiento
#6
costo_llenado = precio_litro * litros_agua
#7
costo_total = costo_revestimiento + costo_llenado
#8
porcentaje_desperdicio = total_revestimiento * 1.1
#9
costo_mas_iva = costo_total * 1.21
margen_ganancia = costo_mas_iva * 0.15

#SALIDAS
print(f"1. El area de la base es: {area_base} m2")
print(f"2. El volumend el agua es: {volumen_de_agua} m3")
print(f"3. Se necesitan {total_revestimiento} m2 de revestimiento")
print(f"4. Se necesitan {litros_agua} litros de agua")
print(f"5. El costo del revestimiento sera: ${costo_revestimiento}")
print(f"6. El costo de llenar la piscina es de: ${costo_llenado}")
print(f"7. Costo total: ${costo_total}")
print(f"8. El total de revestimiento mas el desperdicio: {porcentaje_desperdicio} m2")
print(f"9. El costo total mas IVA 21% es de: ${costo_mas_iva}")
print(f"10. El margen de ganancia es de: ${margen_ganancia}")
