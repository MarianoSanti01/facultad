from tp7functions import*
from ordenamientos import*
#1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.
entry= input("Ingrese una lista de numeros separada por espacios: para el ordenamiento burbuja")
numbers= [int(x) for x in entry.split()]

bubble_sort(numbers)

print("Lista ordenada en orden ascendente: ")
for i in numbers:
    print(i, end=" ")

print(" ")
print("_______________________________")
print(" ")
#2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.
entry= input("Ingrese una lista de palabras separada por espacios para el ordenamiento de seleccion ")
words= entry.split()

selection_sort(words)

print("Lista ordenada alfabeticamente en orden ascendente")
print(words, end=" ")

print(" ")
print("_______________________________")
print(" ")
#3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor, año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.
books = [
    {
        "titulo": "Libro 1",
        "autor": "Autor1",
        "anio_publicacion":2020
    },
        {
        "titulo": "Libro 2",
        "autor": "Autor2",
        "anio_publicacion":2018
    },
        {
        "titulo": "Libro 3",
        "autor": "Autor1",
        "anio_publicacion":2019
    },
        {
        "titulo": "Libro 4",
        "autor": "Autor3",
        "anio_publicacion":2017
    },
]

ordered_books = []
while books:
    lower_index= order_books(books,'anio_publicacion')
    ordered_books.append(books.pop(lower_index))

for book in ordered_books:
    print(f"Titulo: {book['titulo']}, Autor: {book['autor']}, año de publicacion: {book['anio_publicacion']}")

print(" ")
print("_______________________________")
print(" ")
#4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción.

input_strings= input("ingrese una lista de cadenas separadas por comas para el ordenamiento de insercion: ")
strings= input_strings.split(",")

insertion_sort(strings)

print("Cadenas ordenadas por longitud ascendente: ")
for string in strings:
    print(string.strip())


print(" ")
print("_______________________________")
print(" ")
#5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente.

entry= input("Ingrese una lista de numeros separada por espacios: ")
numbers= [int(x) for x in entry.split()]

bubble_sortinv(numbers)

print("Lista ordenada en orden descendente: ")
for i in numbers:
    print(i, end=" ")

print(" ")
print("_______________________________")
print(" ")
#6.	Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de ordenamiento por conteo.
entry= input("Ingrese una lista de numeros separada por espaicos: ")
numbers= [int(x) for x in entry.split()]

sorted_numbers= counting_sort(numbers)
print("Lista ordenada por conteo:")
print(sorted_numbers)

print(" ")
print("_______________________________")
print(" ")
#7.	Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que ordene esta lista de manera que primero estén los números ordenados de menor a mayor y luego las cadenas de caracteres ordenadas alfabéticamente.
my_list=[5,"Manzana",2,"Banana","Pera",1,"Uva"]
ordered_list = order_nums_and_chains(my_list)

print(ordered_list)
#8.	Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números.

entry= input("Ingrese una lista de numeros separada por espacios: para el merge sort ")
numbers= [int(x) for x in entry.split()]

merge_sort(numbers)

print("Lista ordenada en orden ascendente: ")
for i in numbers:
    print(i, end=" ")
