from tp8functions import*
# 1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
number=int(input("Ingrese un numero y la funcion devolvera la cantidad de digitos que este tenga "))
digitscount(number)

# 2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.
n=int(input("Ingrese el numero "))
b=int(input("ingrese la base "))
if potency(n,b):
    print(f"{n} es potencia de {b}")
else:
    print(f"{n} no es potencia de {b}")

# 3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a. Ejemplo:

string1=input("Ingresa una frase ")
string2=input("Ingresa una palabra para hallarla en la frase anterior ")

positions=findstring(string1,string2)
print(positions)

# 4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
# •	1 es impar.
# •	Si un número es impar, su antecesor es par; y viceversa.
number=int(input("Ingrese un numero para deteriminar si este es par o impar "))
if pair(number):
    print(f"{number} Es par")
else:
    print(f"{number} Es impar")
# 5.	Escribir una función recursiva que encuentre el mayor elemento de una lista.
numlist=[]
entry=input("Ingrese los numeros separados por espacio ")
numlist=entry.split(" ")

higher=higherelement(numlist)
print("El Mayor numero de la lista es:", higher)

# 6.	Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces. Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])
listnum=[]
entry=input("Ingrese una lista de numeros separada por espacios ")
listnum=entry.split(" ")
multiplier=int(input("Ingrese la cantidad de veces que desea multiplicar el numero "))
newlist=[]
newlist=multipliernum(listnum,multiplier)
print(newlist)

# 7.	Implemente un algoritmo, usando una función recursiva, que resuelva la siguientesumatoria:
# K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
# ● El programa debe pedir al usuario que ingrese un número n, y un número d,
# ● Luego debe calcular el valor de K(n, p) usando una función recursiva,
# ● Debe imprimir el resultado de K(n, p)

n= int(input("Ingrese el valor de n: "))
p= int(input("Ingrese el valor de P: "))

result= calculate_sumatory(n,p)
print("El resultado de K(n,p) es:", result)

# 8.	El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). Los valores que se encuentran en los bordes del triángulo son todos unos. Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba. Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k.
file = 4
column = 2
result = pascal(file, column)
print(f"El valor en la fila {file} y columna {column} del Triángulo de Pascal es {result}")
# 9.	Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, y un número k, e imprima todas las posibles cadenas de longitud k formadas con los caracteres dados (permitiendo caracteres repetidos).
characters = ['a', 'b', 'c']
long = 2
combinations(characters, long)
# 10.	La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4 (210 mm de ancho y 297 mm de largo). Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. A partir de la A0 las siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N). Siempre se miden en milímetros con números enteros: entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo.

# Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva el ancho y el largo de la hoja A(N) calculada recursivamente a partir de las medidas de la hoja A(N−1), usando la hoja A0 como caso base. La función debe devolver el ancho y el largo -en ese orden- en una tupla.
N = int(input("Ingrese el tamaño de la hoja"))
width, long = measurements_sheet_A(N)
print(f"Las medidas de la hoja A{N} son: {width} mm de ancho y {long} mm de largo.")