
from tp6f import*
primary_names=[]
secondary_names=[]


#Ejercicio 1 + ejercicio 2 + ejercicio 3 + ejercicio 4 + ejercicio 5
from funciones_dimensionales import *
data=[]
while True:
    num=int(input("ingrese en numero \n"))
    if num==0:
        break
    else:
        data=add_in_list(data,num)
print("datos ingresados")
show_list(data)
d_num=int(input("igrese numero para eliminar\n"))
deleate_from_list(data,d_num)
print("los datos ingresados menos el eleminado:\n",)
show_list(data)
sum_data=sum_list_elements(data)
print("la suma de los numero en la lista es ",sum_data)
num1=int(input("ingrese un numero y se filtraran todos los mayores dejando solo los que sean menores al numero ingresado\n"))
data=filter_lower_numbers_from_list(data,num1)
print(data)
data_and_counter=count_same_elements_in_list(data)
print(data_and_counter)
print("---FIN---")

print(" ")
print("______________________________________________________________________________________________")
print(" ")
#EJERCICIO 6

primary_names = []
secondary_names = []

# Solicitar nombres de estudiantes
x=2
while x != 0:
    if x ==2:
        names= input("Ingrese nombre de estudiante de primaria, ingrese una x para salir ").title()
        if names != 'X':
            primary_names.append(names)
        else:
            x-=1
            print(" ")
    elif x==1:
        names= input("Ingrese nombre de estudiante de secundaria, ingrese una x para salir ").title()
        if names != "X":
            secondary_names.append(names)
        else:
            x-=1
            print(" ")

#Imprimir nombres sin repetir
print(" ")
print("Nombres")
all_names = set(primary_names+secondary_names)
for name in all_names:
    print(name)

#Imprimir nombres repetidos
print(" ")
print("Nombres repetidos")
repeated_names= set(primary_names) & set(secondary_names)
for name in repeated_names:
    print(name)

#Imprimir nombres que no se repiten
print(" ")
print("Nombres de primaria que no se repiten en secundaria")
primary_names_no_repeat= set(primary_names) - set(secondary_names)
for name in primary_names_no_repeat:
    print(name)

print(" ")
print("______________________________________________________________________________________________")
print(" ")
#EJERCICIO 7

ocurrency={}
string_counts=0

#Contador hasta 50 en el que pide las cadenas
while string_counts < 50:
    chain = input("Ingrese una cadena ").upper()
    string_counts +=1
    
    #Lector de caracteres y ocurrencias
    for character in chain:
        if character in ocurrency:
            ocurrency[character] +=1
        else:
            ocurrency[character]=1

for character, cuantity in ocurrency.items():
    print(f"'{character}': {cuantity}")

print(" ")
print("______________________________________________________________________________________________")
print(" ")
#Ejercicio 8
# Definir el cuadro de goles en un arreglo de dos dimensiones
goals = [
    [0, 2, 1, 3, 4, 0, 1, 2, 3, 0],
    [1, 0, 2, 0, 1, 2, 0, 1, 0, 1],
    [1, 0, 0, 2, 0, 1, 0, 1, 2, 0],
    [0, 3, 2, 0, 1, 0, 2, 0, 3, 0],
    [4, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 2, 0, 0, 2],
    [2, 1, 0, 2, 1, 2, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 2, 0, 1, 1],
    [3, 2, 0, 1, 1, 0, 0, 2, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0]
]

# Inicializar listas para almacenar victorias, empates, perdidas, goles marcados y goles recibidos
wins = [0] * 10
equals = [0] * 10
loses = [0] * 10
goals_given = [0] * 10
goals_received = [0] * 10

# Calcular los resultados de los partidos
for i in range(10):
    for j in range(10):
        if i != j:
            goals_team_i = goals[i][j]
            goals_wins_j = goals[j][i]
            if goals_team_i > goals_wins_j:
                wins[i] += 1
            elif goals_team_i < goals_wins_j:
                loses[i] += 1
            else:
                equals[i] += 1
            goals_given[i] += goals_team_i
            goals_received[i] += goals_wins_j

# Calcular los puntos obtenidos por cada equipo (3 puntos por triunfo, 1 punto por empate)
points = [wins[i] * 3 + equals[i] for i in range(10)]

# Mostrar los resultados para cada equipo
for i in range(10):
    print(f"Equipo {i + 1}: victorias: {wins[i]}, empates: {equals[i]}, Derrotas: {loses[i]}")
    print(f"Goles marcados: {goals_given[i]}, Goles recibidos: {goals_received[i]}")
    print(f"Diferencia de Goles: {goals_given[i] - goals_received[i]}, Puntos: {points[i]}\n")

print(" ")
print("______________________________________________________________________________________________")
print(" ")
#Ejercicio 9
from variables_dimensionales import*
rows = 4
columns = 4
board = create_board(rows, columns)
selected = []
found = 0

while found < (rows * columns) // 2:
    print_board(board, selected)

    try:
        row_1 = int(input("Selecciona una fila (0-3): "))
        column_1 = int(input("Selecciona una columna (0-3): "))
    except ValueError:
        print("Entrada no válida. Por favor, ingresa valores enteros.")
        continue

    if (
        row_1 < 0
        or row_1 >= rows
        or column_1 < 0
        or column_1 >= columns
    ):
        print("Selección fuera de rango. Por favor, elige nuevamente.")
        continue

    if (row_1, column_1) in selected:
        print("Esta carta ya ha sido seleccionada. Elige otra.")
        continue

    selected.append((row_1, column_1))
    print_board(board, selected)

    try:
        row_2 = int(input("Selecciona otra fila (0-3): "))
        column_2 = int(input("Selecciona otra columna (0-3): "))
    except ValueError:
        print("Entrada no válida. Por favor, ingresa valores enteros.")
        continue

    if (
        row_2 < 0
        or row_2 >= rows
        or column_2 < 0
        or column_2 >= columns
    ):
        print("Selección fuera de rango. Por favor, elige nuevamente.")
        continue

    if (row_2, column_2) in selected:
        print("Esta carta ya ha sido seleccionada. Elige otra.")
        continue

    selected.append((row_2, column_2))
    print_board(board, selected)

    if board[row_1][column_1] == board[row_2][column_2]:
        found += 1
        print("¡Encontraste una pareja!")
        board[row_1][column_1] = 0
        board[row_2][column_2] = 0
    else:
        print("No es una pareja. Intenta de nuevo.")

    selected = []

print("¡Felicidades! Has encontrado todas las parejas.")

print(" ")
print("______________________________________________________________________________________________")
print(" ")
#EJERCICIO 10

# Ingrese la dimensión de la matriz cuadrada
n = int(input("Ingrese la dimensión de la matriz cuadrada: "))

# Inicialice una matriz vacía
matrix = []

# Leer la matriz de entrada
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Ingrese el elemento en la fila {i} y la columna {j}: "))
        row.append(element)
    matrix.append(row)

# Imprimir la matriz ingresada
print("Matriz ingresada:")
for row in matrix:
    print(row)

# Obtener la diagonal principal
main_diagonal = [matrix[i][i] for i in range(n)]

# Obtener la diagonal inversa
reverse_diagonal = [matrix[i][n - 1 - i] for i in range(n)]

# Imprimir las diagonales
print("Diagonal Principal:", main_diagonal)
print("Diagonal Inversa:", reverse_diagonal)


print(" ")
print("______________________________________________________________________________________________")
print(" ")
#ejercicio 11
from funciones_dimensionales import *
dictionary={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa=input("ingrese la divisa a consultar\n").lower()
validation=exist_dictionary(dictionary,divisa)
if validation:
    data=search_value_in_dictionary(dictionary,divisa)
    print("el simolo de ",divisa," es ",data)
else:
    print("no se encontro la divisa ingresada")

print(" ")
print("______________________________________________________________________________________________")
print(" ")
#ejercicio 12
from funciones_dimensionales import *

dictionary={}
name=input("ingrese su nombre\n").lower()
age=int(input("ingrese su edad\n"))
adrees=input("ingrese su dirección\n").lower()
dictionary=add_element_in_dictionary(dictionary,"name",name)
dictionary=add_element_in_dictionary(dictionary,"age",age)
dictionary=add_element_in_dictionary(dictionary,"adress",adrees)
print(dictionary)

print(" ")
print("______________________________________________________________________________________________")
print(" ")
#ejercicio 13
from funciones_dimensionales import *
fruits={}
while True:
    fruit=input("Ingrese nombre de la fruta\n").lower()
    validation1=exist_dictionary(fruits,fruit)
    if not validation1:
        price=int(input("esa fruta no esta registrada ingrese el precio para guardarla\n"))
        fruits=add_element_in_dictionary(fruits,fruit,price)
        kg=int(input("ingrese los kilogramos\n "))
        price_given=search_value_in_dictionary(fruits,fruit)
        total=price_given*kg
    else:
        kg=int(input("ingrese los kilogramos\n "))
        price_given=search_value_in_dictionary(fruits,fruit)
        total=price_given*kg
    print("valor por kg de ",fruit," es ",price_given,"por los ",kg," kg's pedidos el total a pagar es de ",total)

