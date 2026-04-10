
# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.


print("1. -Temporada de Invierno-")
print("2. -Temporada de Verano-")
print("3. -Temporada de Otoño-")
print("4. -Temporada de Primavera-")
opciones = input("Ingrese alguna de las siguientes opciones: ")
match opciones:
    case "1":
        print("Durante la temporada de Invierno solo hay viajes para Bariloche")
    case "2":
        print("Durante la temporada de Verano hay viajes para Mar Del Plata y las Cataratas.")
    case "3":
        print("Durante la temporada de Otoño podes viajar a todos los lugares turisticos")
    case "4":
        print("Durante la temporada de Primavera podes viajar a todos los lugares turisticos menos a bariloche")