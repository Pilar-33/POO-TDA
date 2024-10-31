from os import system
system("cls")

#2- Clase para representar un Rectángulo Crear una clase rectángulo que tenga las
#características base y altura. Del rectángulo se debe poder calcular el área y el perímetro.
#Se debe crear la clase e implementarla.

class Rectangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura
        
    def calcular_area(self) -> None:
        area = self.base * self.altura
        print(f"""
                    EL ÁREA DEL RECTÁNGULO
        ==============================================
                    area = {self.base} * {self.altura} = {area}""")
    
    def calcular_perimetro(self) -> None:
        perimetro = 2 * (self.base + self.altura)
        print(f"""
                        EL PERÍMETRO DEL RECTÁNGULO
        =================================================
                area = 2 * ({self.base} + {self.altura}) = {perimetro}""")
        
rectangulo = Rectangulo(15, 20.5)
rectangulo.calcular_area()
rectangulo.calcular_perimetro()