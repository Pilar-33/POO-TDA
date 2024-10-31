from os import system
system("cls")

from ejercicio1.funciones import*
from ejercicio1.auxiliares import*

alumnos = [
        {"nombre": "Juan", "apellido": "Pérez", "edad": 18, "curso": "Curso Python"},
        {"nombre": "Ana", "apellido": "García", "edad": 19, "curso": "Curso Python"},
        {"nombre": "Luis", "apellido": "Martínez", "edad": 17, "curso": "Curso Python"},
        {"nombre": "Carla", "apellido": "Medina", "edad": 25, "curso": "Curso Python"}
    ]

# Carga de cursos
cursos = [
    {(1, 117): {"cantidad_alumnos": 30, "preceptor": "María"}},
    {(2, 129): {"cantidad_alumnos": 18, "preceptor": "Carlos"}},
    {(1, 149): {"cantidad_alumnos": 25, "preceptor": "María"}},
    {(4, 289): {"cantidad_alumnos": 32, "preceptor": "Juan"}}
]

ejecutar = True
while ejecutar == True:
    opcion  = input(f"""
                MENÚ PRINCIPAL
        ==================================
        1. Carga secuencial de alumnos.
        2. Cargar lista de cursos.
        3. Preceptores por año'.
        4. Promedio de edad de un curso.
        5. Preceptores se encuentran repetidos 
        en dos años distintos.
        6. Preceptores que encuentran solo en 
        un determinado año.
        7- Nombre y apellido del alumno más jóven 
        y más grande del colegio.
        8. Salir  
    Elija una opción (1 al 8): """)
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8"]
    while opcion not in numeros:
        opcion = input("Error!!. Ingrese una opción (1 al 8): ")
    
    match opcion:
        case "1":
            #cantidad_alumnos = validar_numero("Cuántos alumnos desea cargar?: ")
            #alumnos = cargar_alumnos(cantidad_alumnos)
            print(alumnos)  
            print("Alumnos cargados correctamente!")
        case "2":
            #cantidad_cursos = validar_numero("Cuántos cursos desaa agregar?: ")
            #cursos = carga_cursos(cantidad_cursos)
            
            for i, curso in enumerate(cursos):
                (anio, division), info = list(curso.items())[0]
                print(f"""
                    CURSO {i + 1}
                =====================
                Año: {anio}
                División: {division}
                Cantidad de alumnos: {info["cantidad_alumnos"]}
                Preceptor: {info["preceptor"]}
                """)
        case "3":
            preceptores_anio = {}
            for curso in cursos:
                (anio, division), info = list(curso.items())[0]
                preceptor = info["preceptor"]
                if anio not in preceptores_anio:
                    preceptores_anio[anio] =set()
                    preceptores_anio[anio].add(preceptor)
            
            print("\nPRECEPTORES POR AñO\n" + "=" * 25)
            for anio, preceptores in preceptores_anio.items():
                print(f"Año: {anio}")
                print(f"Preceptor: {', '.join(preceptores)}")
        case "4":
            curso = "Curso Python"
            promedio = promedio_edad(alumnos, curso)
            print(f"El promedio de edad de los alumnos del curso {curso} es: {promedio} años.")
        case "5":
            preceptores_repetidos = repetidos(cursos)
            print(f"Los preceptores repetidos son: {preceptores_repetidos}")
        case "6":
            preceptores = preceptores_unico_anio(cursos)
            print("Preceptores asignados a un único año:", preceptores)
        case "7":
            resultado = encontrar_joven_grande(alumnos)
            # Imprimimos los resultados
            print(f"Alumno más joven: {resultado['nombre_joven']}  {resultado['apellido_joven']} con edad {resultado['edad_joven']}")
            print(f"Alumno más grande: {resultado['nombre_grande']} {resultado['apellido_grande']} con edad {resultado['edad_grande']}")
        case "8":
            print("Hasta luego!!")
            ejecutar = False
    
            
    