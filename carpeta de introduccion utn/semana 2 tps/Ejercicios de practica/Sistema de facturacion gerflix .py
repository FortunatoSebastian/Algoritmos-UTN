import os
os.system("cls")
# plan_basico = 5000
# plan_estandar = 8000
# plan_premium = 12000

#ENTRADA
print("-" * 50)
plan = input("Cual plan quiere contratar |Basico, Estandar o Premium|:  ").lower()
dispositivos_adicionales = int(input("Ingrese cuantos dispositivos vinculo a su cuenta: "))
tiempo_de_suscripcion = int(input("Cuantos meses de suscripcion tienes?: "))
usuario = input("Usted es estudiante?: ").lower() == "si"

#PROCESOS

#OPCIONES DE PLANES
if plan == "basico":
    tarifa_base = 5000
elif plan == "estandar":
    tarifa_base = 8000
elif plan == "premium":
    tarifa_base = 12000
else:
    print("Este plan no existe.")
    tarifa_base = 0

#COSTO EXTRA POR DISPOSITIVO
costo_por_dispositivos = dispositivos_adicionales * 500

#COSTO SIN DESCUENTOS
costo_total = tarifa_base + costo_por_dispositivos

descueto_por_plan = 0

# 1-Si el usuario es estudiante y contrata el plan básico, tendrá el siguiente descuento sobre el costo del servicio:
# Un 7% si tiene 3 o más dispositivos.
# Un 10% si tiene más de 5 dispositivos.
# Un 3% si solo tiene 1 o 2 dispositivos.
if usuario and plan == "basico":
    if dispositivos_adicionales >= 3:
        descueto_por_plan = 0.07
    elif dispositivos_adicionales > 5:
        descueto_por_plan = 0.10
    else:
        descueto_por_plan = 0.03

# 2-Si el usuario no es estudiante y contrata el plan estándar, tendrá un descuento del 15% si y sólo si solicita conexión para un solo dispositivo. Si es estudiante, recibe el descuento de todas formas.
if plan == "estandar":
    if not usuario and dispositivos_adicionales == 1:
        descueto_por_plan = 0.15
    elif usuario:
        descueto_por_plan = 0.15

# 3- Si el usuario contrata el servicio premium y es estudiante recibirá un descuento del 20% si la cantidad de dispositivos está entre 5 y 9 inclusive. En caso que no se cumpla nada de lo anterior, solo recibirá un descuento del 5%.

if usuario and plan == "premium":
    if dispositivos_adicionales >= 5 and dispositivos_adicionales <= 9:
        descueto_por_plan = 0.20
    else:
        descueto_por_plan = 0.05



# 4- Usuario activo:
# Si el usuario ha mantenido la suscripción activa por más de 12 meses, recibe un descuento adicional del 10%.
# Si el usuario ha mantenido la suscripción activa por más de 24 meses, el descuento adicional será del 15%.

if tiempo_de_suscripcion > 12:
    descueto_por_meses_activo = 0.10
elif tiempo_de_suscripcion > 24:
    descueto_por_meses_activo = 0.15
else:
    descueto_por_meses_activo = 0

#ESTO ES DE LOS DESCUENTOS
total_descueto_por_plan = tarifa_base * descueto_por_plan
total_descuento_por_antiguedad = tarifa_base * descueto_por_meses_activo
total_descuento = total_descuento_por_antiguedad + total_descueto_por_plan


#Recargos por Uso Excesivo:
# Si el usuario comparte la cuenta con más de 6 dispositivos diferentes (sin importar el plan), se aplica un recargo del 20% sobre el costo del plan contratado.

if dispositivos_adicionales > 6:
    recargo_exceso_dispositivos = tarifa_base * 0.20
else:
    recargo_exceso_dispositivos = 0

#SUB TOTAL ANTES DEL IVA

costo_total = tarifa_base - total_descuento + dispositivos_adicionales + recargo_exceso_dispositivos

#IVA
iva = costo_total * 1.21

costo_final = costo_total + iva
#SALIDAS
print("-" * 50)
print(f"Tipo de plan: {plan}")
print(f"Recargos por dispositivos adicionales: ${costo_por_dispositivos}")
print(f"Descuentos por plan: |{descueto_por_plan*100:.0f}%|: ${total_descueto_por_plan:.2f}" )
print(f"Descuentos por meses activos: |{descueto_por_meses_activo*100:.0f}%|: ${total_descuento_por_antiguedad:.2f}")
print(f"Recargo por uso excesivo de dispositivos: ${recargo_exceso_dispositivos:.2f}")
print("-" * 50)
print(f"Subtotal : ${costo_total}")
print(f"Recargos por impuesto IVA 21%: ${iva:.2f}")
print("-" * 50)
print(f"TOTAL A PAGAR: ${costo_final:.2f}")
print("-" * 50)

