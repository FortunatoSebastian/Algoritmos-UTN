#Entrada
print("-" * 50)
mts_consumidos = float(input("Ingresar cantidad de mts consumidos: "))
tipo_de_cliente = input("Ingrese que tipo de cliente es usted: ").lower()

#Proceso
costo_por_mt3 = 200
total_por_consumo = mts_consumidos * costo_por_mt3
tarifa_base = total_por_consumo + 7000
impuesto_iva = tarifa_base * 1.21
total_a_pagar = impuesto_iva + tarifa_base
print("-" * 50)
print(f"Consumo Total sin descuentos/recargos aplicados: ${total_por_consumo}")

if tipo_de_cliente == "residencial":
    if tarifa_base > 35000:
        total_por_consumo = total_por_consumo * 0.95 # -5%
        print("---Se agrego un descuento adicional por consumo bajo---")

    if mts_consumidos < 30:
        total_por_consumo = total_por_consumo * 0.90
    elif mts_consumidos > 80:
        total_por_consumo = total_por_consumo * 1.15
    else:
        total_por_consumo == total_por_consumo

if tipo_de_cliente == "comercial":
    if mts_consumidos > 150:
        total_por_consumo = total_por_consumo * 0.92 # -8%
    elif mts_consumidos > 300:
        total_por_consumo = total_por_consumo * 0.88 # -12%
    elif mts_consumidos < 50:
        total_por_consumo = total_por_consumo * 1.05 # +5%

if tipo_de_cliente == "industrial":
    if mts_consumidos > 500:
        total_por_consumo = total_por_consumo * 0.80 # -20%
    elif mts_consumidos > 1000:
        total_por_consumo = total_por_consumo * 0.70 # -30%
    elif mts_consumidos < 200:
        total_por_consumo = total_por_consumo * 1.10 # +5%

#Salida

print(f"Consumo Total con descuentos/recargos aplicados: ${total_por_consumo}")
print(f"Subtotal a pagar: ${tarifa_base:.2f}")
print(f"Aplicacion del impuesto IVA (21%): ${impuesto_iva}")
print(f"Total final a pagar es: ${total_a_pagar}")
