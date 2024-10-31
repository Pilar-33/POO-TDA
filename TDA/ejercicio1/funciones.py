from .auxiliares import validar_numero
def cargar_alumnos(cantidad_alumnos: int) -> dict:
    alumnos = []
    for i in range(cantidad_alumnos):
                print(f"\nALUMNO(A) nro{i + 1}\n" + "=" * 20)
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                edad = validar_numero("Edad: ")
                curso = ("Curso Python")

                #crear diccionario alumnos
                alumno = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "edad": edad,
                    "curso": curso
                }
                alumnos.append(alumno)
    return alumnos

def carga_cursos(cantidad_cursos: int) -> dict:
    cursos = []
    for i in range(cantidad_cursos):
            anio = validar_numero("Año del curso: ")
            division = validar_numero("División del curso: ")
            nro_alumno = validar_numero("Cantidad de alumnos: ")
            preceptor = input("Nombre del preceptor a cargo: ")
                
            curso = {
                (anio, division): {
                    "cantidad_alumnos": nro_alumno,
                    "preceptor":  preceptor
                    }
                }
            cursos.append(curso)
    return cursos

def promedio_edad(alumnos: list, curso) -> float:
    suma_edades = 0
    contador = 0
    for alumno in alumnos:
        if alumno["curso"] == curso:
            suma_edades += alumno["edad"]
            contador += 1
        
    if contador == 0:
        return "No  hay alumnos cargados en el curso"
    else:
        promedio =  suma_edades / contador
    return promedio
    
def repetidos(cursos: list) -> list:
    repetidos = []
    precetores_anios = []
    for curso in cursos:
        for (anio, _), datos in curso.items():
            preceptor = datos["preceptor"]
            if (preceptor in precetores_anios and
            anio != precetores_anios[preceptor] and 
            preceptor not in repetidos):
                repetidos.append(preceptor)
            else:
                precetores_anios[preceptor] = anio
    return repetidos

def preceptores_unico_anio(cursos: list) -> list:
    preceptores_anio = {}  
    
    for curso in cursos:
        for (anio, division), datos in curso.items():
            preceptor = datos["preceptor"]
            
            # Crear la clave del preceptor para el diccionario
            clave_preceptor = (preceptor, anio)
            
            # Si la clave no está en el diccionario, la añadimos con un conjunto vacío
            if clave_preceptor not in preceptores_anio:
                preceptores_anio[clave_preceptor] = set()
            
            # Añadir la división al conjunto del preceptor
            preceptores_anio[clave_preceptor].add(division)
    
    # Filtrar preceptores que solo están asignados a un único año y división
    preceptores_solo_anio = []  #
    for (preceptor, anio), divisiones in preceptores_anio.items():
        if len(divisiones) == 1:  
            preceptores_solo_anio.append((preceptor, anio))
    
    return preceptores_solo_anio  

def encontrar_joven_grande(alumnos: dict) -> dict:
    edad_joven = None
    nombre_joven = None
    apellido_joven = None
    edad_grande = None
    nombre_grande = None
    apellido_grande = None
    
    for alumno in alumnos:
        edad = alumno["edad"]
        nombre = alumno["nombre"]
        apellido = alumno["apellido"]
        
        if edad_joven is None or edad < edad_joven:
            edad_joven = edad
            nombre_joven = nombre
            apellido_joven = apellido
        
        if edad_grande is None or edad > edad_grande:
            edad_grande = edad
            nombre_grande = nombre
            apellido_grande = apellido
    
    rpta = {
        "nombre_joven": nombre_joven,
        "apellido_joven": apellido_joven,
        "edad_joven" : edad_joven,
        "nombre_grande": nombre_grande,
        "apellido_grande": apellido_grande,
        "edad_grande": edad_grande
    }
    
    return rpta
    