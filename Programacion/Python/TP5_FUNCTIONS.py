import math
#EJ1 y 3
def dnivalidator(document,documentvalidator):
    dnistr=str(document)
    if len(dnistr) == 8 or len(dnistr) == 7:
        documentvalidator=True
        return documentvalidator
    else:
        documentvalidator=False
        return documentvalidator
#EJ2
def lastphraselong(phrase_):
    phrase_=phrase_.split()
    lastphrase=phrase_[-1]
    return len(lastphrase)
#EJ3
# Función para generar el identificador único
def generate_identifier(first_name_, last_name_, dni_):
    first_name_ = first_name_.split()[0]
    last_name_length = len(last_name_)
    first_three_digits_dni = dni_[:3]
    return f"{first_name_}{last_name_length}{first_three_digits_dni}"
#EJ 4 
def is_multiple(num1, num2):
    if num2 == 0:
        return False  
    return num1 % num2 == 0
#EJ5
# Definir la función para calcular la temperatura media
def calculate_average_temperature(max_temp, min_temp):
    return (max_temp + min_temp) / 2
#EJ6
def add_space_after_letters(text):
    result = ""
    for letter in text:
        if letter != " ":
            result += letter + " "
        else:
            result += " "
    return result
#EJ7
# Función para encontrar el valor máximo y mínimo en una lista de números
def find_max_and_min(numbers):
    if not numbers:
        return None, None 
    maximum = minimum = numbers[0]  
    for number in numbers:
        if number > maximum:
            maximum = number
        elif number < minimum:
            minimum = number
    return maximum, minimum

#EJ8
def calcular_area_y_perimetro(radio):
    area = math.pi * radio ** 2

    perimetro = 2 * math.pi * radio

    return area, perimetro

#EJ9
def login(username, password, attempts):
    if username == "usuario1" and password == "asdasd":
        return True, attempts
    else:
        attempts += 1
        return False, attempts

#EJ10
def apply_discount(cart, discounts):
    total_price = 0

    for product, price in cart.items():
        if product in discounts:
            discounted_price = price - (price * discounts[product] / 100)
            total_price += discounted_price
        else:
            total_price += price

    return total_price

#EJ11
def apply_function_to_list(func, input_list):
    result_list = []
    for item in input_list:
        result_list.append(func(item))
    return result_list

def square(number):
    return number ** 2

#EJ12
def word_lengths(sentence):
    words = sentence.split()
    result = {}
    for word in words:
        result[word] = len(word)
    return result

#EJ13
def calculate_module_vector(vecto_r):
    module_ = math.sqrt(sum(component ** 2 for component in vecto_r))
    return module_

#Ej14
def is_prime(number_):
    if number_ <= 1:
        return False
    for i in range(2, number_):
        if number_ % i == 0:
            return False
    return True

#Ej15
def factorial(number_):
    if number_ == 0:
        return 1
    else:
        return number_ * factorial(number_ - 1)

#Ej16
# Función para calcular la frecuencia de un dígito en un número
def calculate_digit_frequency(number, digit):
    frequency = 0
    temp_number = number
    
    while temp_number > 0:
        current_digit = temp_number % 10
        if current_digit == digit:
            frequency += 1
        temp_number //= 10
    
    return frequency

#Ej17
# Función para calcular el factorial de un número
def calculate_factorial(number):
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    return factorial

# Función para calcular la suma de los dígitos de un número
def calculate_digit_sum(number):
    digit_sum = 0
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number //= 10
    return digit_sum





