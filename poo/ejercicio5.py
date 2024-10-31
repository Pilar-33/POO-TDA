from os import system
system("cls")

"""
5- Encapsulamiento Crear una clase Cuenta Bancaria que 
tenga las características titular y
saldo encapsulado. De la cuenta bancaria se puede obtener 
el saldo, depositar o retirar (en cada caso imprimir que fue exitoso). 
Se debe crear la clase e implementarla.
"""
class Cuenta_Bancaria:
    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.__saldo = saldo
    
    def obtener_saldo(self) -> float:
        return self.__saldo
    
    def depositar(self, monto: float) -> None:
        if monto > 0:
            if monto <= self.__saldo:
                self.__saldo += monto
                print(f"Deposito exitoso. Saldo actual: USD {monto}")
            else:
                print("El monto a depositar debe ser mayor a cero.")
    
    def retirar(self, monto: float) -> None:
        if monto > 0:
            if monto <= self.__saldo:
                self.__saldo -= monto
                print(f"Retiro exitoso. Saldo actual: USD {monto}")
            else:
                print(f"El monto a retirar debe ser menor o igual a USD {self.__saldo} .")
                
cuenta = Cuenta_Bancaria("Pilar Guitierrez", 1000.89)
print(f"El saldo inicial: USD {cuenta.obtener_saldo()}")

#Depositar
cuenta.depositar(150.80)

#retirar
cuenta.retirar(500)