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
    precetores_dict = {}
    for curso in cursos:
        for (anio, _), datos in curso.items():
            preceptor = datos["preceptor"]
            if (preceptor in precetores_dict and
            anio != precetores_dict[preceptor] and 
            preceptor not in repetidos):
                repetidos.append(preceptor)
            else:
                precetores_dict[preceptor] = anio
    return repetidos
    
    