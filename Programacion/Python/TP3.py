"""#Ejercicio 1
print("1-	Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.")

word = input("Ingrese una palabra y será mostrada diez veces ")
i=0
while i < 10 :
    i=i+1
    print(word)

print("______________________________________________________________________")
#Ejercicio 2
print("2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).")

age=int(input("Ingrese su edad, para hacer una linea del tiempo"))
i=1

while i <= age :
    print(i)
    i=i+1

print("______________________________________________________________________")
#Ejercicio 3
print("Números impares hasta...")
number = int(input("Ingrese un número: "))
i = 1
while i <= number:
    if (i%2==1):
        print(i, end=",")
    i += 1
print(" ")
    
print("______________________________________________________________________")
#Ejercicio 4
number = int(input("Ingrese un número: "))
i = 1
while i <= number:
    number=number-1
    print(number, end=",")
print(" ")

print("______________________________________________________________________")
#Ejercicio 5
print("Calculadora de inversión")
investment = float(input("Ingrese la cantidad de dinero que desea invertir:"))
annual_interest = float(input("Ingrese el interés anual:"))
number_of_years = int(input("ingrese la cantidad de años"))
for i in range(number_of_years):
    investment += (investment * annual_interest)/100
    print(f"La ganancia del año {i+1} es: {investment} ")
print("______________________________________________________________________")
#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
#*
#**
#***
#****
print("Triángulo de asteriscos")
heigth = int(input("Ingrese la altura del triángulo:"))
#para cada linea repetir 1 de altura
asterisco=""
for i in range(heigth):
    asterisc = asterisc + "*"
    print(asterisc)


print("______________________________________________________________________")
#Ejercicio 7
#Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10
print("Tablas de multiplicar")
for i in range(1,11):
    for f in range(1,11):
        print(f"{i} x {f} = {i*f}")

print("______________________________________________________________________")
#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
#1
#21
#321
#4321
print("Triángulo de números")
number = input("Ingrese un número entero: ")
number_ = ""
for i in range(len(number)):
    number_ =  number[i] + number_
    print(number_)


print("______________________________________________________________________")

#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
print("Validación de contraseña")
password = "uwu"
validator= ""
while validator != password:
    validator = input("Ingrese la contraseña:")

print("______________________________________________________________________")

#Ejercicio 10
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
print("¿Primo o no primo?")
prime = 0
number = int(input("Ingrese un número: "))
for n in range (2, number-1):
    if number%n==0:
        prime += 1
if (prime > 0):
    print("No es primo")
else:

    print("Es primo")


print("______________________________________________________________________")

#Ejercicio 11
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
#hola
#aloh
print("Invertir palabra")
word = input("Ingrese una palabra: ")
for i in reversed(word):
    print(i)


print("______________________________________________________________________")

#Ejercicio 12
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra emn la frase.
print("Buscador de caracteres")
phrase = input("Ingrese una frase: ")
letter = input("Ingrese una letra: ")
count = 0
for i in phrase:
    if (i == letter):
        count += 1

if (count > 0):
    print(f"Se encontró la letra {count} veces")
else:
    print("No se encontró la letra")


print("______________________________________________________________________")

#Ejercicio 13
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
print("Introduzca una palabra y salir para salir")
exit_ = "salir"
validator= ""
while validator != exit_:
    print(validator)
    validator = input("")


print("______________________________________________________________________")

#Ejercicio 14
#Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.
print("Pares o impares entre dos numeros")
num_a = int(input("Ingrese el primer número: "))
num_b = int(input("Ingrese el segundo número: "))
for i in range (num_a, num_b):
    if i%2==0:
        print(f"{i}, es par")
    else:
        print(f"{i}, es impar")
"""
print("______________________________________________________________________")

#Ejercicio 15
#Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

print("Los divisores de un número")

num= int(input("Ingrese un numero para mostrar sus divisores"))

for i in range(1,num+1):
    if num%i==0:
        print(i ," es divisor de ", num)
        
