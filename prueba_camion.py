import os
os.system("cls")
tipo_vehiculo = input("Tipo vehiculo: ")
km = int(input("Km acumulado: "))

if tipo_vehiculo == "auto":
    if km < 10000:
        mantenimiento = "básico"
    elif km <=50000:
        mantenimiento = "preventivo"
    else: 
        mantenimiento = "general"

elif tipo_vehiculo == "moto":
    if km < 5000:
        mantenimiento = "cambio de aceite"
    elif km <=20000:
        mantenimiento = "Ajuste general"
    else:
        mantenimiento = "Revisión completa"

else:
    peso = input("Ingresa el peso del camión: ")

    match peso: 
        case "liviano":
            mantenimiento = "Revisión cada 15,000 km"
        case "mediano":
            mantenimiento = "Revisión cada 10,000 km"
        case _:
            mantenimiento = "Revisión cada 5,000 km"


print(f"Mantenimiento recomendado: {mantenimiento}")