from os import system
class Persona():
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Cliente(Persona):
    
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de Cuenta {self.numero_cuenta}: ${self.balance}"

    def depositar(self, monto_deposito):
        system("cls")
        print("*" * 50)
        self.balance += monto_deposito
        print("Deposito aceptado")
        print("*" * 50)

    def retirar(self, monto_retiro):
        system("cls")
        print("*" * 50)
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
            print("*" * 50)
        else:
            print("Fondos insuficientes")
            print("*" * 50)

def Menu_inicio():
    system("cls")
    

def crear_cliente():
    system("cls")
    print("*" * 50)
    nombre_cl = input("Ingrese su Nombre: ")
    apellido_cl = input("Ingrese su Apellido: ")
    numero_cuenta = input("Ingrese su Numero de Cuenta: ")

    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    print("*" * 50)
    return cliente
    

def inicio():
    system("cls")
    mi_cliente = crear_cliente()
    print(mi_cliente)

    opcion = 0

    while opcion != "S" or "s":
        print("Elije: Depositar (D), Retirar (R), o Salir (S)")
        opcion = input()
        print("*" * 50)

        if opcion == "D" or "d":
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == "R" or "r":
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)
        print("*" * 50)
    print("Gracias por operar en Banco el Seba")

inicio()