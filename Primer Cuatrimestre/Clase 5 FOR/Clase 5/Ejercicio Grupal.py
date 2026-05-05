def medir_peso(peso : float, altura: float) -> str:
    ''' 
    Inicializa la variable IMC y divide peso por altura al cuadradado
    y luego comprueba su según su resultado si se debe ingestar
    mas calorias o no o si debe mantenerse
    '''
    imc = peso / (altura ** 2)

    if imc < 18.5:
        analisis_imc = "es necesario aumentar ingesta calorica."
    elif imc < 25:
        analisis_imc = "peso equilibrado."
    else:
        analisis_imc = "es necesario disminuir ingesta calorica."

    return analisis_imc

def medir_temperatura(temperatura: float) -> str:
    '''
    Evalua el valor de la temperatura ingresada 
    y luego comprueba si el paciente tiene mucha fiebre o no
    '''
    if temperatura > 41:
        fiebre = "Muy alta."
    elif temperatura > 39:
        fiebre = "Alta."
    elif temperatura >= 38:
        fiebre = "Fiebre moderada."
    elif temperatura > 37.3:
        fiebre = "Febricula."
    else:
        fiebre = "Temperatura normal."
    
    return fiebre

def medir_presion(presion_sistolica:float, presion_diastolica: float) -> str:
    '''
        Evalua los valores ingresados de Presion
        y comprueba si los valores de presion son normales, altos o bajos
    '''
    if presion_sistolica < 90 or presion_diastolica < 60:
        analisis_presion = "baja"
    elif presion_sistolica > 140 or presion_diastolica > 90:
        analisis_presion = "alta"
    else:
        analisis_presion = "normal"
        
    return analisis_presion

def generar_diagnostico(nombre: str) -> str:
    diagnostico = f"""
    Diagnostico del paciente {nombre}
    Peso: {medir_peso(88 , 1.89)}
    Temperatura: {medir_temperatura(40)}
    Presion: {medir_presion(74, 60)}
    """
    print(diagnostico)

generar_diagnostico("Eduardo")



