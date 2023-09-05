#Ejercicio 1
print("1.	Calcular el perímetro y área de un rectángulo dada su base y su lado")

lado=int(input("ingrese un lado de su rectangulo "))
base=int(input("ingrese la base de su rectangulo "))

perimetro= lado+lado+base+base
area= lado*base

print("El perimetro de su rectangulo es igual a ",perimetro)
print("El area de su rectangulo es igual a ",area)


print("____________________________________________________________________________")

#Ejercicio 2
print("2.	Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.")

cat_1=int(input("ingrese un cateto de su triangulo "))
cat_2=int(input("ingrese el otro cateto de su triangulo "))

hipotenusa=(((cat_1**2)+(cat_2**2))**1/2)
print("La hipotenusa del triangulo es igual a ", hipotenusa)


print("____________________________________________________________________________")

#Ejercicio 3
print("3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.")

num_1=int(input("Ingrese el primer numero "))
num_2=int(input("Ingrese el segundo numero "))

suma= num_1+num_2
resta= num_1-num_2
divi= num_1/num_2
mult= num_1*num_2

print("la suma de sus numeros es", suma)
print("la resta de sus numeros es", resta)
print("la division de sus numeros es", divi)
print("La multiplicacion de sus numeros es", mult)


print("____________________________________________________________________________")

#Ejercicio 4
print("4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.:")

f=int(input("Ingrese sus grados farenheit "))
c=(f-32*5/9)
print("Su temperatura convertida a Es igual a ", c , "grados") 


print("____________________________________________________________________________")

#Ejercicio 5
print("5. Qué problemas tienen las siguientes instrucciones?¿Como solucionarlas?")

print("A = input(nombre, “¿Cuál es tu canción favorita?”)")
print("El problema es que el ejercicio está mal definidio, tiene la variable dentro del imput y una variable A definida por afuera. se solucionaría así")
nombre= input("Cual es su cancion favorita? ")


print("-------")

print("precio = input(“Precio: “)")
print("total = precio + (precio * 0.1)")
print("El problema está en que la variable precio no se define como tipo INT, por lo tanto, el programa no lo toma como un numero, tambien hallé que las comillas no eran las correctas")
precio = int(input("Precio: "))
total = precio + (precio * 0.1)


print("-------")
print("edad = int(input(“Edad: “))")
print("print(tu edad es, edad)")
print("Otra vez las comillas no son las indicadas en la primera linea. y en la segunda linea, el PRINT no tenia comillas dentro.")

edad = int(input("Edad: "))
print("Tu edad es", edad)


print("-------")
print("edad = int(input(“Edad: “))")
print("print(“Veamos si tu edad es 18…”, edad=18)")
print("El error acá es qué en la segunda linea, esta impreso edad=18 y lo tomara invalido, solo admite variables, no datos.")
edad = int(input("Edad: "))
print("Veamos si tu edad es 18… Tu edad es: ", edad)


print("____________________________________________________________________________")

#Ejercicio 6
print("6.	Calcular la media de tres números pedidos por teclado.")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

media = (numero1 + numero2 + numero3) / 3

print("La media de los tres números es:", media)


print("____________________________________________________________________________")

#Ejercicio 7
print("7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.")

minutos = int(input("Ingrese la cantidad de minutos: "))

horas = minutos // 60
minutos_ = minutos % 60

print(f"{minutos} minutos son {horas} horas y {minutos_} minutos.")

print("____________________________________________________________________________")

#Ejercicio 8
print("8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.")

sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))

venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))

comision_total = (venta1 + venta2 + venta3) * 0.1
sueldo_total = sueldo_base + comision_total

print(f"El total de comisiones por las tres ventas es: {comision_total}")
print(f"El sueldo total del vendedor en el mes es: {sueldo_total}")

print("____________________________________________________________________________")

# Ejercicio 9
print("9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.")

total_compra = float(input("Ingrese el total de la compra: "))
descuento = total_compra * 0.15
total_final = total_compra - descuento

print(f"El total a pagar después del descuento es: {total_final}")


print("____________________________________________________________________________")

# Ejercicio 10
print("10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:")
print("55% del promedio de sus tres calificaciones parciales.")
print("30% de la calificación del examen final.")
print("15% de la calificación de un trabajo final.")

parcial1 = float(input("Ingrese la calificación del primer parcial: "))
parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
examen_final = float(input("Ingrese la calificación del examen final: "))
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.3) + (trabajo_final * 0.15)

print(f"La calificación final del alumno en Algoritmos es: {calificacion_final}")


print("____________________________________________________________________________")

# Ejercicio 11
print("11. Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

distancia = abs(numero1 - numero2)

print(f"La distancia entre los números es: {distancia}")


print("____________________________________________________________________________")

# Ejercicio 12
print("12. Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.")

numero = float(input("Ingrese un número: "))
raiz_cuadrada = numero ** 0.5
raiz_cubica = numero ** (1/3)

print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")
print(f"La raíz cúbica de {numero} es: {raiz_cubica}")


print("____________________________________________________________________________")

# Ejercicio 13
print("13. Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.")

numero_dos_cifras = int(input("Ingrese un número de dos cifras: "))
numero_invertido = (numero_dos_cifras % 10) * 10 + (numero_dos_cifras // 10)

print(f"El número invertido es: {numero_invertido}")


print("____________________________________________________________________________")

# Ejercicio 14
print("14. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.")

A = int(input("Ingrese el valor de la variable A: "))
B = int(input("Ingrese el valor de la variable B: "))

A, B = B, A

print(f"El valor de A después del intercambio: {A}")
print(f"El valor de B después del intercambio: {B}")


print("____________________________________________________________________________")

# Ejercicio 15
print("15. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.")

HH = int(input("Ingrese la hora de partida: "))
MM = int(input("Ingrese los minutos de partida: "))
SS = int(input("Ingrese los segundos de partida: "))
T = int(input("Ingrese el tiempo de viaje en segundos: "))

total_segundos = HH * 3600 + MM * 60 + SS + T
llegada_HH = total_segundos // 3600
llegada_MM = (total_segundos % 3600) // 60
llegada_SS = total_segundos % 60

print(f"La hora de llegada a la ciudad B es: {llegada_HH}:{llegada_MM}:{llegada_SS}")


print("____________________________________________________________________________")

# Ejercicio 16
print("16. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.")

nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")

iniciales = nombre[1] + apellido1[1] + apellido2[1]
print(iniciales)

print("____________________________________________________________________________")

# Ejercicio 17
print("17. Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario. A continuación mostrar por pantalla: 'Ahora estás en la matrix, [nombre del usuario]'.")

usuario = input("Ingrese su nombre: ")
print(f"Ahora estás en la matrix, {usuario}")


print("____________________________________________________________________________")

# Ejercicio 18
print("18. Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.")

costo_cena = float(input("Ingrese el costo de la cena en el restaurante: "))
servicio = costo_cena * 0.062
propina = costo_cena * 0.1
monto_final = costo_cena + servicio + propina

print(f"El monto final a pagar es: {monto_final}")


print("____________________________________________________________________________")

# Ejercicio 19
print("19. Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa.")

dia = int(input("Ingrese el día de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento: "))
anio = int(input("Ingrese el año de su nacimiento: "))

print(f"La fecha de nacimiento es: {dia}/{mes}/{anio}")


print("____________________________________________________________________________")

# Ejercicio 20
print("20. Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.")

fecha_nacimiento = int(input("Ingrese su fecha de nacimiento en formato DDMMAAA: "))
dia = fecha_nacimiento // 1000000
mes = (fecha_nacimiento // 10000) % 100
anio = fecha_nacimiento % 10000

print(f"La fecha de nacimiento es: {dia}/{mes}/{anio}")


print("____________________________________________________________________________")

# Ejercicio 21
print("21. Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.")
print("Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.")
print("Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.")

km_por_litro = float(input("Ingrese cuántos kilómetros puede recorrer la moto con 1 litro de combustible: "))
capacidad_tanque = float(input("Ingrese la capacidad del tanque en litros: "))
km_totales = float(input("Ingrese cuántos kilómetros recorrerán en total: "))

tanques_necesarios = km_totales / (km_por_litro*km_totales)

print(f"La cantidad de tanques de combustible necesarios es: {tanques_necesarios}")









