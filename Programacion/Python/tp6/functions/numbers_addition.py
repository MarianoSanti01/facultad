import math
def numbers_addition(number):
    result = 0
    while number>0:
        digit=(number%10)
        result += digit
        number=int(number/10)
    return result
#TP5
def dni_verification(number):
    if(number>99999999 or number<=999999):
        return False
    else:
        return True
    
def long_last_word(phrase):
    words= phrase.split(" ")
    return len(words[-1])

def individual_token(name,surname,dni):#mejorar
    token=""
    data1=surname.split(" ")
    if (len(data1)>1):
        print("---ERROR ingrese un solo apellido---")
        return token
    else:
        data=name.split(" ")
        if len(data)>=3:
            print("---ERROR ingrese uno o dos nombres---")
            return token
        elif (len(data) >= 2):
            first_name=data[0]
            second_name=data[1]
            token += first_name[0]+first_name[1]+second_name[0]+second_name[1]+surname[0]+surname[1]+dni[0]+dni[1]
            return token
        else:
            first_name=data[0]
            token += first_name[0]+first_name[1]+surname[0]+surname[1]+dni[0]+dni[1]
            return token
def multiple(num1,num2):
    counter=0
    for i in range(num2):
        if (i*num1==num2):
            counter += 1
    if(counter!=0):
        return True
    else:
        return False

def middle_temp(max_temp,minimal_temp):#revisar
    mid=max_temp-minimal_temp
    return mid

def phrase_with_spaces(phrase):
    new_phrase=""
    for i in phrase:
        if i != " ":
            new_phrase+=i+" "
    return new_phrase

def lowest_biggest(numbers):
    lowest=numbers[0]
    biggest=numbers[0]
    for i in numbers:
        if i>biggest:
            biggest=i
        elif i<lowest:
            lowest=i
    data = [biggest,lowest]
    return data
def circuferance_data(radio):
    area= math.pi*(radio**2)
    diameter = 2*radio
    data=[str(round(area, 2)),str(round(diameter,2))]
    return data
def loggin(username,password):
    if (username!="usuario1" and password != "asdasd"):
        print("---usuario y contraseña equivocados---")
        return False
    elif (username != "usuario1"):
        print("---ususario equivocado---")
        return False
    elif(password!="asdasd"):
        print("---contraseña equivocada---")
        return False
    else:
        return True
def discount(shop_cart):
    discount_applied=[]
    for i in shop_cart.items():
        discount_operation=round(i[1][0]-(i[1][0]*i[1][1]/100),2)
        discount_applied.append(discount_operation)
    return discount_applied
def called(n):
    return n[0]*n[1]
 
def caller(func, n):
    return func(n)
def create_dictionary(phrase):
    dictionary={}
    splited_phrase=phrase.split(" ")
    for i in splited_phrase:
        dictionary.update({i:len(i)})
    return dictionary
def sum_squares(square,total):
    total += square**2
    return total
def is_prime_number(num):
    counter=0
    for i in range(num):
        if(num%(i+1)==0):
            counter+=1
    if (counter != 2):
        return False
    else:
        return True
def facorial(num,total):
    for i in range(num):
        total*=i+1
    return total
def show_facorial(num,total):
    for i in range(num):
        print(total," * ",i+1," = ",(total*(i+1)))
        total*=i+1
    return total
def sigle_digit_verification(digit):
    if(digit>=10):
        return False
    else:
        return True
def number_verification(num):
    if type(num)!=int:
        return False
    else:
        return True
def digit_times_in_number(num,digit):
    counter=0
    while num>0:
        aux=num%10
        if(aux==digit):
            counter+=1
        num=int(num/10)
    return counter