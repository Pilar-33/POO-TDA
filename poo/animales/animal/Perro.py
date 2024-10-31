from animal.Animal import Animal

class Perro(Animal):
    def __init__(self, nombre: str, sonido:  str) -> None:
        super().__init__(nombre)
        self.sonido = sonido
    
    def hacer_sonido(self):
        print(f"El perro se llama {self.nombre} y realiza el sonido: {self.sonido}")