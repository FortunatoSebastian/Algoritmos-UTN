import os
os.system("cls")
tipo_vehiculo = input("Ingresa el tipo de vehiculo(automovil, motocicleta, camion): ")
kilometraje = int(input("Ingresa el kilometraje acumulado del vehiculo: "))

if tipo_vehiculo == "automovil":
    if kilometraje < 10000:
        mantenimiento = "Mantenimiento basico"
    elif kilometraje <= 50000:
        mantenimiento = "Mantenimiento preventivo"
    else:
        mantenimiento = "Mantenimiento general"

elif tipo_vehiculo == "motocicleta":
    if kilometraje < 5000:
        mantenimiento = "Cambio de aceite"
    elif kilometraje <= 20000:
        mantenimiento = "Ajuste general"
    else:
        mantenimiento = "Revesion completa"

else:
    peso = input("Ingresa el peso del camion (liviano, mediano, pesado): ")
    match peso:
        case "liviano":
            mantenimiento = "Revision cada 15,000 km"
        case "mediano":
            mantenimiento = "Revision cada 10,000 km"
        case _:
            mantenimiento = "Revision cada 5,000 km"

    if kilometraje > 100000:
        mantenimiento += "- ¡Revision urgente recomendada!"

print(f"Mantenimiento recomendado: {mantenimiento}")