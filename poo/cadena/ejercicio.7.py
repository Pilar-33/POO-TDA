from os import system
system("cls")

"""Ejercicio 7: Desarrollar una función “ordenar” 
que recibe un string y un número (1 o
-1). Se debe retornar el string ordenado de manera 
ascendente (si recibió 1 por
parámetros) o descendente (si recibió -1)
Nota: Determinar parámetros y retornos de manera que 
las funciones sean
genéricas y reutilizables"""

def ordenar_string(mensaje: str, numero: int) -> str:
    if numero == 1:
        ordenado = ''.join(sorted(mensaje))
    elif numero == -1:
        ordenado = ''.join(sorted(mensaje, reverse=True))
    
    return ordenado

print(ordenar_string("palabra", 1))
print(ordenar_string("palabra", -1))
