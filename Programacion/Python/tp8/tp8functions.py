def digitscount(number,counter=0):
    if number > 0:
        number = number//10
        return digitscount(number,counter+1)
    else:
        print(f"El numero tiene {counter} digitos")
        return counter

