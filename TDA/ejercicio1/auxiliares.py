
def validar_numero(mensaje: str) -> int:
    entrada  = input(mensaje)
    es_valido = True
    
    for caracter in entrada:
        if caracter < '0' and caracter > '9':
            es_valido = False
            break
        
    if es_valido == True and len(mensaje) > 0:
        return int(entrada)
    else:
        print("Número no válido!!!")
    