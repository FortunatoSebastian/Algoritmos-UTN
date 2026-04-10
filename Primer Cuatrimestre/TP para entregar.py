import os
os.system("cls")

mts_consumidos = float(input("Ingresar cantidad de mts consumidos: "))

costo_por_mt3 = 200
total_por_consumo = mts_consumidos * costo_por_mt3

print("1 - Residencial")
print("2 - Comercial")
print("3 - Industrial")

tipo_cliente = input("Ingrese el tipo de Cliente: ")

match tipo_cliente:
    case "1": #Residencial
        if ((total_por_consumo + 7000) < 35000):
            total_por_consumo = total_por_consumo * 0.95
        if mts_consumidos < 30:
            total_por_consumo = total_por_consumo * 0.90
        elif mts_consumidos > 80:
            total_por_consumo = total_por_consumo * 1.15
    case "2": #Comercial
        if mts_consumidos > 150:
            total_por_consumo = total_por_consumo * 0.92
        elif mts_consumidos > 300:
            total_por_consumo = total_por_consumo * 0.88
        elif mts_consumidos < 50:
            total_por_consumo = total_por_consumo * 1.05
    case "3": #Industrial
        if mts_consumidos > 500:
            total_por_consumo = total_por_consumo * 0.80
        elif mts_consumidos > 1000:
            total_por_consumo = total_por_consumo * 0.70
        elif mts_consumidos < 200:
            total_por_consumo = total_por_consumo * 1.10

tarifa_base = total_por_consumo + 7000
impuesto_iva = tarifa_base * 0.21
total_a_pagar = tarifa_base + impuesto_iva
print("=" * 50)
print(f"Consumo Total con descuentos/recargos aplicados: ${total_por_consumo:.2f}")
print(f"Subtotal a pagar: ${tarifa_base:.2f}")
print(f"Impuesto IVA (21%): ${impuesto_iva:.2f}")
print(f"Total final a pagar es: ${total_a_pagar:.2f}")
print("=" * 50)