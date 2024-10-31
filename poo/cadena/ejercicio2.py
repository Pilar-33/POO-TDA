from os import system
system("cls")

#Ejercicio 2: Desarrollar una función que cuente cuántas palabras 
# hay en una cadena.

def contar_palabras(mensaje: str ) -> int:
    """
    Esta función cuenta cuántas palabras hay en una cadena.
    """
    palabras = mensaje.split()
    return len(palabras)

mensaje = "Es un día grandioso"
contar = contar_palabras(mensaje)
print(contar)