from TP5_FUNCTIONS import*
"""1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
"""
dni=int(input("Ingrese su DNI, SIN PUNTOS "))
validator=False
validator=dnivalidator(dni,validator)
if validator==True:
    print("Su documento es correcto")
else:
    print("Documento no valido")

"""
2.	Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.
"""
phrase=input("Ingrese una frase con espacios ").strip()

long=lastphraselong(phrase)
print(f"La ultima palabra tiene una longitud de {long}")
"""
3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
Nombre: María Ines Rosales
DNI: 25469648
ID -> Maria7254
"""

identifiers = {}

while True:
    full_name = input("Ingrese el nombre completo del socio (o un nombre vacío para finalizar): ").strip()

    if full_name == "":
        break
    validator_2=False
    if validator_2==False:
        print("El número de DNI debe tener 7 u 8 dígitos.")
        dni = input("Ingrese el número de DNI del socio (7 u 8 dígitos): ").strip()
        validator_2= dnivalidator(dni,validator_2)

    names = full_name.split()
    first_name = names[0]
    last_name = names[-1]

    identifier = generate_identifier(first_name, last_name, dni)

    identifiers[full_name] = identifier

print("Identificadores únicos de los socios:")
for full_name, identifier in identifiers.items():
    print(f"Nombre Completo: {full_name} | ID: {identifier}")
"""
4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
"""
number1 = int(input("Ingrese el primer número entero: "))
number2 = int(input("Ingrese el segundo número entero: "))

if is_multiple(number1, number2):
    print(f"{number1} es múltiplo de {number2}.")
elif is_multiple(number2, number1):
    print(f"{number2} es múltiplo de {number1}.")
else:
    print("Ninguno de los números es múltiplo del otro.")

"""
5.	Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
"""
num_days = int(input("Ingrese el número de días para los que desea calcular la temperatura media: "))

average_temperatures = []

for day in range(1, num_days + 1):
    max_temperature = float(input(f"Ingrese la temperatura máxima del día {day}: "))
    min_temperature = float(input(f"Ingrese la temperatura mínima del día {day}: "))

    average_temperature = calculate_average_temperature(max_temperature, min_temperature)
    average_temperatures.append(average_temperature)

    print(f"La temperatura media del día {day} es: {average_temperature}°C")

overall_average_temperature = sum(average_temperatures) / num_days
print(f"La temperatura media general es: {overall_average_temperature}°C")
"""
6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.
"""
text_ = input("Ingrese un texto: ")

result_ = add_space_after_letters(text_)

print("El texto con espacios adicionales tras cada letra es:")
print(result_)
"""
7.	Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
"""
input_text = input("Ingrese una lista de números separados por espacios: ")

numbers_list = [float(num) for num in input_text.split()]

max_value, min_value = find_max_and_min(numbers_list)

if max_value is not None and min_value is not None:
    print(f"El valor máximo es: {max_value}")
    print(f"El valor mínimo es: {min_value}")
else:
    print("La lista está vacía, no se puede encontrar el máximo y mínimo.")
"""
8.	Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
"""
try:
    radio = float(input("Ingrese el radio de la circunferencia: "))

    area, perimetro = calcular_area_y_perimetro(radio)

    print(f"El área de la circunferencia es: {area}")
    print(f"El perímetro de la circunferencia es: {perimetro}")
except ValueError:
    print("Por favor, ingrese un valor numérico válido para el radio.")

"""
9.	Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
"""
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    login_exitoso, attempts = login(username, password, attempts)

    if login_exitoso:
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Nombre de usuario o contraseña incorrectos. Intentos restantes:", max_attempts - attempts)

if attempts == max_attempts:
    print("Se han agotado los intentos. Cierre de sesión.")
"""
10.	Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra.
"""
cart = {
    "product1": 50,
    "product2": 30,
    "product3": 20
}

discounts = {
    "product1": 10,
    "product3": 15
}

final_price = apply_discount(cart, discounts)
print(f"El precio final de la compra con descuento es: {final_price}")
"""
11.	Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
"""
numbers = [1, 2, 3, 4, 5]

results = apply_function_to_list(square, numbers)

print("Lista de números:", numbers)
print("Resultado después de aplicar la función square:", results)
"""
12.	Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
"""
frase = "Bajen la dificultad de la UTN"
diccionario_resultado = word_lengths(frase)

print("Frase:", frase)
print("Diccionario con la longitud de las palabras:", diccionario_resultado)

"""
13.	Escribir una función que calcule el módulo de un vector.
"""
vector = (3, 4, 5)
module = calculate_module_vector(vector)

print("Vector:", vector)
print("Módulo del vector:", module)

"""
14.	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.
"""
try:
    number = int(input("Ingrese un número entero: "))
    if is_prime(number):
        print(f"{number} es un número primo.")
    else:
        print(f"{number} no es un número primo.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
"""
15.	Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.
"""
total_numbers = 0

while True:
    try:
        number = int(input("Ingrese un número entero (o -1 para salir): "))
        if number == -1:
            break
        total_numbers += 1
        factorial_result = factorial(number)
        print(f"El factorial de {number} es: {factorial_result}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

print(f"Total de números leídos: {total_numbers}")

"""
16.	Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia.
"""
try:
    user_number = int(input("Ingrese un número entero: "))
    user_digit = int(input("Ingrese un dígito: "))
    
    if 0 <= user_digit <= 9:
        digit_frequency = calculate_digit_frequency(user_number, user_digit)
        print(f"El dígito {user_digit} aparece {digit_frequency} veces en el número {user_number}.")
    else:
        print("Por favor, ingrese un dígito válido (0-9).")
except ValueError:
    print("Por favor, ingrese un número entero válido y un dígito válido.")
"""
17.	Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.
"""
prime_number = True
largest_number = 0

while prime_number:
    try:
        number = int(input("Ingrese un número primo (o un número no primo para finalizar): "))
        
        if number <= 1:
            prime_number = False
        else:
            if is_prime(number):
                digit_sum = calculate_digit_sum(number)
                print(f"La suma de los dígitos de {number} es: {digit_sum}")
                
                digit = int(input("Ingrese un dígito para calcular su frecuencia en el número: "))
                frequency = calculate_digit_frequency(number, digit)
                print(f"El dígito {digit} aparece {frequency} veces en el número {number}.")
                
                if number > largest_number:
                    largest_number = number
            else:
                prime_number = False
    except ValueError:
        print("Por favor, ingrese un número válido.")

if largest_number > 0:
    factorial_largest = calculate_factorial(largest_number)
    print(f"El factorial del mayor número ingresado ({largest_number}) es: {factorial_largest}")
else:
    print("No se ingresaron números primos.")