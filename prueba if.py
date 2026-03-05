import os 
os.system("cls")
materias = int(input("ingrese el número de materias del semestre: "))
promedio = float(input("ingrese su promedio de calificaciones: "))
desempeño = input("ingrese su tipo de desempeño (alto/medio/bajo): ")
print("-"*50)
horas_estudio = 0


if promedio >= 8 and desempeño == "alto":
    horas_estudio = 5
elif promedio < 8 and desempeño == "medio":
    horas_estudio = 7
elif desempeño == "bajo":
    horas_estudio = 10

if materias > 5:
    horas_estudio += 1

total_de_horas = horas_estudio * materias

print(f"debe estudiar {horas_estudio} horas por materia por semana")
print(f"el total de horas de estudio por semana es {total_de_horas}")