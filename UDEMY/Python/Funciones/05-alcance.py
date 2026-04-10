#Contexto global
#por ahora no usar
saludo = "Hola Global"

def saludar():
    global saludo
    saludo = "Hola mundo"

def saludaChanchito():
    saludo = 24
    print(saludo)

print(saludo)
saludar()
print(saludo)
