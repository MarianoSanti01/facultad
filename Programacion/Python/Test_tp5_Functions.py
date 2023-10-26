import pytest
from TP5_FUNCTIONS import * 
#Ej1
def test_dnivalidator():
    assert dnivalidator(436357190,True)==False
#Ej2
def test_lastphraselong():
    assert lastphraselong("animales caninos")==7
    assert lastphraselong("Perros bonitos")==7
    assert lastphraselong("Hola como va")==2
#Ej3
def test_generate_identifier():
    assert generate_identifier("Mariano","Santi","43635719")=="Mariano5436"
    assert generate_identifier("Mariano","Santi","43745719")=="Mariano5437"
    assert generate_identifier("Mariano","Santi","43855719")=="Mariano5438"

#Ej 4
def test_is_multiple():
    assert is_multiple(12, 3) == True
    assert is_multiple(20, 5) == True
    assert is_multiple(100, 10) == True

#Ej5
def calculate_average_temperature():
    max_temp = 30
    min_temp = 10
    assert calculate_average_temperature(max_temp, min_temp) == 20.0

#EJERCICIO 17
def test_calculate_factorial():
    assert calculate_factorial(5) == 120
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1

def test_calculate_digit_sum():
    assert calculate_digit_sum(12345) == 15
    assert calculate_digit_sum(0) == 0
    assert calculate_digit_sum(999) == 27

def test_calculate_digit_frequency():
    assert calculate_digit_frequency(12345, 3) == 1
    assert calculate_digit_frequency(123321, 2) == 2
    assert calculate_digit_frequency(987654, 0) == 0

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(4) == False
#EJ11
def test_square():
    assert square(0) == 0
    assert square(5) == 25
    assert square(-4) == 16
    assert square(2.5) == 6.25