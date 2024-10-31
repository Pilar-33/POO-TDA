from os import system
system("cls")

"""Ejercicio 6: Desarrollar una función que verifique 
si una cadena es un palíndromo:
Palíndromo: Palabra o frase cuyas letras están dispuestas 
de tal manera que resulta la misma leída de izquierda a 
derecha que de derecha a izquierda; por ejemplo,
anilina"""

def es_palindromo(mensaje: str) -> str:
    mensaje = mensaje.replace(" ", "").lower()
    invertir = mensaje[::-1]
    return invertir

#palabra = "anilina"
#palabra= "texto"
palabra = "Seres"
palabra_modificada = palabra.replace(" ", "").lower()
invertida = es_palindromo(palabra)

if  invertida == palabra_modificada:
    print(f"La palabra {palabra} es un palíndromo: {invertida}")
else:
    print(f"La palabra {palabra} no es un palíndromo: {invertida}")
    