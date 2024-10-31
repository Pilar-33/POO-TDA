from os import system
system("cls")

#2- Clase para representar una Calculadora Crear una clase Calculadora que pueda calcular
#suma, resta, multiplicación y división. Se debe crear la clase e implementarla.

class Calculadora:
    def __init__(self, num1: float, num2: float) -> None:
        self.num1 = num1
        self.num2 = num2
    
    def sumar(self) -> float:
        suma = self.num1 + self.num2
        return suma
    
    def restar(self) -> float:
        resta = self.num1 - self.num2
        return resta
    
    def multiplicar(self) -> float:
        producto = self.num1 * self.num2
        return producto
    
    def dividir(self) -> float:
        if self.num2 == 0:
            division = "No se puede dividir por cero."
        else:
            division = self.num1 / self.num2
        return division
num1 = 12
num2 =  2 

calculadora = Calculadora(num1, num2)
print(f"""
                    OPERACIONES
        ====================================
        * Suma: {num1} + {num2} = {calculadora.sumar()}
        * Resta: {num1} - {num2} = {calculadora.restar()}
        * Multiplicación: {num1} * {num2} = {calculadora.multiplicar()}
        * División: {num1} / {num2} = {calculadora.dividir()}""")

