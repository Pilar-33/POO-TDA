from os import system
system("cls")

'''Ejercicio 4: Desarrollar una función que convierta los elementos de lista_peli en una
cadena y muestre:
ej. "Se recomienda ver "Matrix", "El Padrino" y "Titanic" "" para cada elemento
lista_peli = [
["Matrix", "El Padrino", "Titanic"],
["Forrest Gump", "Pulp Fiction", "Gladiador"],
["Blade Runner", "El Rey León", "Volver al Futuro"],
["La La Land", "El Gran Lebowski", "Blade Runner"],
["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
["Harry Potter", "Forrest Gump", "Pulp Fiction"],
["Titanic", "Star Wars", "El Señor de los Anillos"],
["The Truman Show", "The Shape of Water", "The Big Lebowski"],
["Forrest Gump", "The Godfather", "Goodfellas"],
["The Terminator", "The Sixth Sense", "The Great Gatsby"]
]'''

def recomendar_peliculas(list_peli):
    for sublista in list_peli:
        cadena = "Se recomienda ver "
        for pelicula in sublista:
            cadena += pelicula + ", "
        print(cadena[:-2])  
        
lista_peli = [
["Matrix", "El Padrino", "Titanic"],
["Forrest Gump", "Pulp Fiction", "Gladiador"],
["Blade Runner", "El Rey León", "Volver al Futuro"],
["La La Land", "El Gran Lebowski", "Blade Runner"],
["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
["Harry Potter", "Forrest Gump", "Pulp Fiction"],
["Titanic", "Star Wars", "El Señor de los Anillos"],
["The Truman Show", "The Shape of Water", "The Big Lebowski"],
["Forrest Gump", "The Godfather", "Goodfellas"],
["The Terminator", "The Sixth Sense", "The Great Gatsby"]
]
        
recomendar_peliculas(lista_peli)
