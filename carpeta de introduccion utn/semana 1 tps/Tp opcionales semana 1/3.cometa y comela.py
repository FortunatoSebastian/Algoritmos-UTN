import os
os.system("cls")
lado_menor = float(input("Ingresa el valor del lado menor: "))/100 #B-C
diagonal_menor = float(input("Ingresa el valor del diagonal menor: "))/100 #C-D
lado_mayor = float(input("Ingresa el valor del lado mayor: "))/100 #D-A


#PASO 1
x1 = (lado_menor**2 - (diagonal_menor/2)**2)**0.5
x2 = (lado_mayor**2 - (diagonal_menor/2)**2)**0.5

#PASO 2
diagonal_mayor = x1 + x2

#PASO 3
perimetro = 2*lado_menor + (2*lado_mayor)

#PASO 4
varilla = perimetro + diagonal_mayor + diagonal_menor

#PASO 5 AREA

area_chica = ((diagonal_menor/2) * x1)/2
area_grande =((diagonal_menor/2) * x2)/2
area_total = (area_chica * 2) + (area_grande * 2)
papel_por_cometa = area_total * 1.1

#PASO 6

papel_total = papel_por_cometa * 10


print(f"Papel Total - {papel_total:.2f} m²")
print(f"Metros de varilla en total - {varilla * 10:.2f} m")



