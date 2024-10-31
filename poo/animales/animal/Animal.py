from os import system
system("cls")

"""4- Herencia de clases
Crear una clase Animal que tenga la característica nombre. La clase Perro que herede de
Animal las características y realice el sonido “guau guau”. La clase Gato que herede de
Animal las características y realice el sonido “Miau”. Del gato y el perro se debe poder
mostrar el sonido que realizan. Se debe crear la clase e implementarla."""

class Animal:
    def __init__(self, nombre: str) -> None:
        self.nombre =  nombre
        
    