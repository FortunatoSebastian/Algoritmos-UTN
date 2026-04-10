import numeros
from os import system

def preguntar():
    system("cls")
    print("Bienvenido a farmacia el seba")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            mi_rubro = input("\nElija su rubro: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            break
    numeros.decorador(mi_rubro)

def inicio():
    system("cls")
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break
    
inicio()