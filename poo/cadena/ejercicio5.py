from os import system
system("cls")

# Ejercicio 5: Desarrollar una función que capitalice palabras en una cadena.
def capitalizar_palabras(mensaje: str) -> str:
    """
    Función que hace que la primera letra del string mayúsculas
    y el resto en minúsculas.
    """
    palabras = mensaje.split()
    
    capitalizadas = []
    
    for palabra in palabras:
        capitalizadas.append(palabra.capitalize())
        
    capitaliza = " ".join(capitalizadas)
    return capitaliza

mensaje = "cien años de soledad"
capital = capitalizar_palabras(mensaje)
print(capital)