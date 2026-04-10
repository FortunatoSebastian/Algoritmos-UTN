import random
#lista inicial
palitos = ['-','--','---','----','-----',]

#mezclar palitos
def mezclar(lista):
    random.shuffle(lista)
    return lista

#pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4','5']:
        intento = input("ingrese un numero del 1 al 5: ")
    return int(intento)

# intento1 = probar_suerte()
# print(intento1)
#comprobar intento

def chequear_intento(lista,intento):
    if lista[intento -1] == '-':
        print("Perdiste ")
    else:
        print("Ganaste ")
    
    print(f"te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)