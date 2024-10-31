from os import system
system("cls")

# 1-Clase para representar un Libro
#Crear una clase Libro que tenga las características título, autor y año de publicación. Del
#libro se debe poder obtener información, mostrando por mensaje todos sus datos. Se debe
#crear la clase e implementarla.

class Libro:
    def __init__(self, titulo: str, autor: str, anio: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        
    def mostrar_datos(self) -> None:
        print(f"""
            INFORMACIÓN DEL LIBRO
        =============================
        Título: {self.titulo}
        Autor: {self.autor}
        Año: {self.anio}""")
        
libro = Libro("Cien años de Soledad", "Gabriel García Márquez", 1967)
libro.mostrar_datos()