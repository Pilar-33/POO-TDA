from os import system
system("cls")

#Ejercicio 1: Desarrollar una función que Invierte el 
# orden de los caracteres en una cadena.

def invertir_slancing(mensaje: str) -> str:
    """
    Esta función invierte el orden de los caracteres 
    en una cadena.
    """
    invertir = mensaje[::-1]
    return invertir

def invertir_cadena(mensaje: str) -> str:
    """
    Esta función invierte el orden de los caracteres 
    en una cadena.
    """
    invertida = ""
    for i in range(len(mensaje) - 1, -1, -1):
        invertida += mensaje[i]
    return invertida

def invertir(mensaje: str) -> str:
    """
    Esta función invierte el orden de los caracteres 
    en una cadena utilizando una lista y el método reverse().
    """
    lista_mensaje = list(mensaje)
    lista_mensaje.reverse()
    invertir = ''.join(lista_mensaje)
    return invertir

mensaje = "Hola Mundo"
print(invertir_slancing(mensaje))
print(invertir_cadena(mensaje))
print(invertir(mensaje))
    