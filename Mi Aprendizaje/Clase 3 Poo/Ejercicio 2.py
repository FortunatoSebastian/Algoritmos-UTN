import os
os.system("cls")
# Ejercicio 2 — Medio:
# Creá una clase CuentaBancaria con atributo saldo. Agregá dos métodos: depositar(monto) que sume al saldo, y mostrar_saldo() que lo imprima. Probala depositando dos veces y mostrando el saldo.

class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo = self.saldo + monto

    def mostrar_saldo(self):
        print(self.saldo)

cuenta1 = CuentaBancaria(1000)

cuenta1.depositar(3000)

cuenta1.mostrar_saldo()