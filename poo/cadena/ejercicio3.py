from os import system
system("cls")

# Ejercicio 3: Desarrollar una función que reemplaza 
# una palabra específica por otra en una cadena.

def reemplazar(mensaje: str, palabra: str, palabra_reemplazo: str) -> str:
    """
    Esta función reemplaza una palabra específica por otra en una cadena.
    """
    mensaje_nuevo = mensaje.replace(palabra, palabra_reemplazo)
    return mensaje_nuevo

mensaje = "Hoy es un día soleado"
print(f"Mensaje original: {mensaje}")

remplaza = reemplazar(mensaje, "soleado", "gris")
print(f"Mensaje modificado: {remplaza}")
