#Ej1
def digitscount(number,counter=0):
    if number > 0:
        number = number//10
        return digitscount(number,counter+1)
    else:
        print(f"El numero tiene {counter} digitos")
        return counter
#EJ2
def potency(n,b):
    if n < 1 or b <2:
        return False
    if n == 1:
        return True
    if n%b!=0:
        return False
    return potency(n//b,b)

#EJ3

def findstring(str1,str2, start=0):
    position=str1.find(str2,start)
    if position == -1:
        return []
    
    next_positions= findstring(str1,str2, position+1)
    return [position] +next_positions

#Ej4

def pair (number):
    if number==0:
        return True
    else:
        return impair(number-1)
def impair(number):
    if number==0:
        return False
    else:
        return pair(number-1)
    

#EJ5
def higherelement(listnum, num=0, higher=None):
    if num==len(listnum):
        return higher
    current_element=listnum[num]
    if higher is None or current_element >higher:
        higher=current_element
    return higherelement(listnum,num+1,higher)

#EJ6

def multipliernum(numlist, multiplier):
    if multiplier > 1:
        return numlist + multipliernum(numlist, multiplier - 1)
    else:
        return numlist
    
#EJ7

def calculate_sumatory(n, p):
    if n == 1:
        return p
    else:
        return n * p + calculate_sumatory(n - 1, p)
    
#Ej8
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)
    
#EJ9
def combinations(list, k, prefix=""):
    if k == 0:
        print(prefix)
        return
    for character in list:
        new_prefix = prefix + character
        combinations(list, k - 1, new_prefix)
#Ej10
def measurements_sheet_A(N):
    if N == 0:
        return (841, 1189)

    previous_width, previous_long = measurements_sheet_A(N - 1)

    width = previous_long // 2
    
    long = previous_width

    return (width, long)