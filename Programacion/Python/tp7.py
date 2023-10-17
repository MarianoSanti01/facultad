from tp7functions import*
from ordenamientos import*
#1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.
entry= input("Ingrese una lista de numeros separada por espacios: ")
numbers= [int(x) for x in entry.split()]

bubble_sort(numbers)

print("Lista ordenada en orden ascendente: ")
for i in numbers:
    print(i, end=" ")

print(" ")
print("_______________________________")
print(" ")
#2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.
entry= input("Ingrese una lista de palabras separada por espacios ")
words= entry.split()

selection_sort(words)

print("Lista ordenada alfabeticamente en orden ascendente")
print(words, end=" ")

print(" ")
print("_______________________________")
print(" ")
#3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor, año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.
books = [
    {"titulo": "Libro A", "autor": "Autor X", "año_publicacion": 2000},
    {"titulo": "Libro B", "autor": "Autor Y", "año_publicacion": 1995},
    {"titulo": "Libro C", "autor": "Autor Z", "año_publicacion": 2010},
    {"titulo": "Libro D", "autor": "Autor X", "año_publicacion": 2015},
]

bubble_sortdic
print("Libros ordenados por año de publicacion: ")
for books in books_sorted_by_year:
    print(f"Título: {books['titulo']}, Autor: {books['autor']}, Año de Publicación: {books['año_publicacion']}")

print(" ")
print("_______________________________")
print(" ")
#4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción.

#5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente.

#6.	Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de ordenamiento por conteo.

#7.	Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que ordene esta lista de manera que primero estén los números ordenados de menor a mayor y luego las cadenas de caracteres ordenadas alfabéticamente.

#8.	Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números.
