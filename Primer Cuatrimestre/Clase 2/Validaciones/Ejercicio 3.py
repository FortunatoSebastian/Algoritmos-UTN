nota = int(input("Ingrese una nota (1 a 10): "))

while nota < 1 or nota > 10:
    print("Error. La nota debe estar entre 1 y 10.")
    nota = int(input("Ingrese una nota (1 a 10): "))

print("Nota válida:", nota)