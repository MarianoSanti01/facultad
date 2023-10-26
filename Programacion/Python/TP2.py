print("1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.")
#Ejercicio 1

antiguedad= int(input("Ingrese cuantos años de antiguedad tiene su computadora "))
if(antiguedad < 3 ):
    print("Su computadora es moderna")
else:
    print("Su computadora es vieja")

print("___________________________________________________________________________")

print("2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.")
#Ejercicio 3
antiguedad= int(input("Ingrese cuantos años de antiguedad tiene su computadora "))
if(antiguedad < 3 and antiguedad > 0):
    print("Su computadora es moderna")
elif(antiguedad > 2):
    print("Su computadora es vieja")
else:
    print("ERROR")

print("___________________________________________________________________________")

print("3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.")
#Ejercicio 3

pname= input("Ingrese el primer nombre ").capitalize()
sname= input("Ingrese el segundo nombre ").capitalize()

if (pname[0] == sname[0]):
    print("Hay coincidencia")
else:
    print("NO HAY COINCIDENCIA")

print("___________________________________________________________________________")

print("4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.")
#Ejercicio 4
voto=input("ingrese que candidato desea votar, CANDIDATO A  por PARTIDO ROJO, CANDIDATO B por PARTIDO VERDE, CANDIDATO C por PARTIDO AZUL ").upper()

if ((voto == "A") or (voto == "B") or (voto == "C")):
    if(voto =="A"):
        print("Usted voto al partido ROJO")
    elif (voto =="B"):
        print("Usted voto al partido VERDE")
    else:
        print("Usted votó al partido AZUL")
else:
    print("Usted votó en blanco")
    pass

print("___________________________________________________________________________")

print("5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.")
#Ejercicio 5

vocal= input("Ingrese una vocal ").capitalize()

if (len(vocal) < 2):
    if ((vocal == "a") or (vocal == "e") or (vocal == "i") or (vocal == "o") or (vocal == "u")):
        print("es una vocal")
    else:
        print("No es una vocal")
else:
    print("No se puede procesar el dato")

print("___________________________________________________________________________")

print("6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.")
#Ejercicio 6

numero= int(input("ingrese un año "))

if(((numero%4 == 0) and not (numero%100 == 0))) or (numero%400 == 0):
    print("Es bisiesto")
else:
    print("No es biciesto")

print("___________________________________________________________________________")

print("7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.")
#Ejercicio 7

num_uno=int(input("ingrese el primer numero "))
num_dos=int(input("ingrese el segundo numero "))
num_tres=int(input("ingrese el tercer numero "))

if(num_uno < num_dos and num_uno < num_tres):
    print("El primer numero es el menor")
elif(num_dos < num_uno and num_dos < num_tres):
    print("El segundo numero es el menor")
elif(num_tres < num_dos and num_tres < num_uno):
    print("El tercer numero es el menor")

print("___________________________________________________________________________")

print("8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.")
#Ejercicio 8 

usuario= input("ingrese un usuario ").capitalize()
clave= input("Ingrese una clave ").capitalize()

if(usuario == "Gwenevere" and clave == "Excalibur"):
    print("Bienvenido a Camelot")
else:
    print("Acceso denegado")

print("___________________________________________________________________________")

print("9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.")
#Ejercicio 9

sexo= input("Ingrese su sexo ").capitalize()
nombre= input("Ingrese su nombre ").capitalize()

if((sexo== "Mujer" and nombre[0]<"M") or (sexo=="Hombre" and nombre[0]>"M")):
    print("Grupo A")
else:
    print("Grupo B")

print("___________________________________________________________________________")

print("10-	Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.")
#Ejercicio 10

edad = int(input("Ingrese su edad, seguido de eso, le daremos un monto a pagar."))

if edad < 4:
    print("ud tiene acceso gratis.")
elif edad >= 4 and edad < 18:
    print("Usted debe de pagar $500")
elif edad >= 18:
    print("Usted debe pagar 1000$")

print("___________________________________________________________________________")

print("11- Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.")
#Ejercicio 11

pizza = input("Bienvenido a pizzería bella napoli, desea una pizza común o vegetariana? ").capitalize()

if pizza == "Vegetariana":
    sabor = input("Los sabores disponibles son: pimiento o tofu. por favor seleccione uno ").capitalize()
    if sabor == "Tofu":
        print("Su pizza contiene: TOMATE, QUESO Y TOFU")
    elif sabor == "Pimiento":
        print("Su pizza contiene: TOMATE, QUESO Y PIMIENTO")
elif pizza == "Comun":
    sabor = input ("Los sabores disponibles son: JAMON, SALMON Y PEPPERONI, por favor elija uno ").capitalize()
    if sabor== "Jamon":
        print("Su pizza contiene TOMATE, QUESO Y JAMON")
    elif sabor== "Salmon" :
        print("Su pizza contiene TOMATE, QUESO Y SALMON")
    elif sabor =="Pepperoni":
        print("Su pizza contiene TOMATE, QUESO y PEPPERONI")

print("___________________________________________________________________________")

print("12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.")
#Ejercicio12

fechaold = int(input("Ingrese una fecha anterior "))
fechahoy = int(input("Ingrese el año actual"))

print("Desde tu fecha pedida, hasta la fecha de hoy, han pasado ", fechahoy-fechaold ," años")

print("___________________________________________________________________________")

print("13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos o nulos.")
#Ejercicio13

num_uno = int(input("ingrese un numero"))
num_dos = int(input("ingrese otro numero"))
if num_uno > 0:
    if num_uno > num_dos:
        print("El numero uno es mayor al dos")
        if num_uno % num_dos:
            print("Es multiplo")
        else:
            print("No es multiplo")
    elif num_dos < num_uno:
        print("El numero dos es mayor al uno")
        if num_dos % num_dos:
            print("Es multiplo")
        else:
            print("No es multiplo")

print("___________________________________________________________________________")

print("14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución. Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a")
#Ejercicio14

a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))

if a == 0:
    if b == 0:
        print("Todos los números son solución.")
    else:
        print("La ecuación no tiene solución.")
else:
    x = -b / a
    print(f"La solución es x = {x}")

print("___________________________________________________________________________")

print("15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.")
#Ejercicio15

repe = input("Ingrese T si quiere ver el area de un triangulo, o C si quiere ver el area de un circulo").capitalize()
if repe == "T":
    base= float(input("Ingrese la base de su TRIANGULO"))
    altura= float(input("Ingrese la altura de su TRIANGULO"))
    print((base*altura)/2)
elif repe == "C":
    radio=float(input("Ingrese el radio de su circulo"))
    print(3.14*(radio**2))

print("___________________________________________________________________________")

print("16-	Haz una calculadora básica pida al usuario dos valores, a y b.")
print(" Según la opción que desean, realizar la operación:")
print("•	Si operación es 1 entonces debemos ver el resultado de a + b")
print("•	Si operación es 2 entonces debemos ver el resultado de a * b")
print("•	Si operación es 3 entonces debemos ver el resultado de a - b")
print("•	Si operación es 4 entonces debemos ver el resultado de a / b")
#Ejercicio16

a=int(input("Ingrese el valor a"))
b=int(input("Ingrese el valor b"))
opcion=int(input("Ingrese qué operacion desea hacer"))

if opcion == 1:
    print("La suma de A y B es igual a",a+b)
elif opcion == 2:
    print("La multiplicacion de A y B es igual a",a*b)
elif opcion == 3:
    print("La resta de A y B es igual a",a-b)
elif opcion == 4:
    print("La division de A y B es igual a",a/b)
else :
    print("ERROR")
print("___________________________________________________________________________")

print("17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.")
#Ejercicio17
dia=input("Ingrese un día de la semana").capitalize()
if dia == "Lunes":
    print("odio lo lune")
elif dia == "Viernes":
    print("Si tomás no manejes")
elif dia == "Sabado" or dia== "Domingo":
    print("Feliz fin de semana")
else: 
    print("No tengo mensaje para este día, pero que te sea prospero")

print("___________________________________________________________________________")

print("18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.")
print("La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.")
print("Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.")
#Ejercicio18

horas= int(input("ingrese la cantidad de horas hechas este mes"))
salario= int(input("ingrese su salario por hora"))

if horas > 48:
    hextra= horas-48
    print("Trabajó ", hextra, " Horas extra")
    sextra= hextra*(((salario*10)/100)+salario)
    print("Su sueldo base es de ", 48*salario ,"$ Teniendo en cuenta qué hizo horas extras se le suman ", sextra ,"$. dando un total de", sextra+(48*salario), "$")
else:
    print("Su sueldo es dé ", horas*salario, "$")

print("___________________________________________________________________________")

print("19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.")
#Ejercicio19
lapices=int(input("Ingrese la cantidad de lapices a comprar"))
precio=60

if lapices >999:
    print("Obtuvo un descuento del 7% por llevar mil o más unidades. Debe pagar ", lapices*(precio-((precio*7)/100)), "$")
else:
    print("Debera pagar ", lapices*precio, "$")
print("___________________________________________________________________________")

print("20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.")
#Ejercicio20

nota1=int(input("Ingrese su primer nota "))
nota2=int(input("Ingrese su segunda nota "))
nota3=int(input("Ingrese su tercera nota "))
nota4=int(input("Ingrese su cuarta nota "))

promedio= (nota1+nota2+nota3+nota4)/4

if promedio >5:
    print("Su nota es ", promedio, " Está aprobado")
elif promedio <6:
    print("Su nota es ", promedio, " Está desaprobado")

print("___________________________________________________________________________")