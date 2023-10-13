''' TUPLE FUNCTIONS '''
#creates a tuple with two elements
def add_two_elements_in_tupla(element1,element2):
    tupla=()
    tupla+=(element1,element2)
    return tupla
#creates a tuple with three elements
def add_three_elements_in_tupla(element1,element2,element3):
    tupla=()
    tupla+=(element1,element2,element3)
    return tupla
#compares a list with a tuple's list and return true or false
def find_tuple_in_list(lis,to_search):
    condition=0
    for i in lis:
        for j in i:
            if(j in to_search):
                condition=1
    if condition!=0:
        return True
    else:
        return False
#check if there is a tuple with an element returns true or false
def existing_value(lis,to_Search):
    for i in lis:
        if to_Search in i:
            return True
    return False
#count how many elements in a tuple's list are in a list of elements
def count_in_list_tuple(lis,to_search):
    counter=0
    for i in lis:
        for j in i:
            if j in to_search:
                counter+=1
    return counter
#return an element of a tuple in a list of tuples
def give_elements(lis,index):
    data=[]
    for i in lis:
        if(i[index]not in data):
            data.append(i[index])
    return data
'''LIST FUNCTIONS'''
#return a list with elements that fulfill a condition
def give_element_in_tupla(lis,to_search,index):
    data=[]
    for i in lis:
        for j in i:
            if(j in to_search):
                data.append(i[index])
    return data
#print a list
def show_list(lis):
    for i in lis:
        print(i)
#count a list
def count_list(lis):
    counter=0
    for i in lis:
        counter+=1
    return counter
#count true and false in list
def count_tof(lis):
    counterT=0
    counterF=0
    for i in lis:
        if i==True:
            counterT+=1
        else:
            counterF+=1
    return[counterT,counterF]
#add elements in list
def add_in_list(data,element):
    data.append(element)
    return data
#deleates an especifict element one time
def deleate_from_list(lis,to_deleate):
    for i in lis:
        if(i==to_deleate):
            index=lis.index(i)
            del lis[index]
            break
#sum all elements in a list
def sum_list_elements(lis):
    total=0
    for i in lis:
        total+=i
    return total
#given a list and number it return a new list with all the numbes lower to the one given
def filter_lower_numbers_from_list(lis,to_compare):
    data=[]
    for i in lis:
        if i<to_compare:
            data.append(i)
    return data
def count_same_elements_in_list(lis):
    data=[]
    for i in lis:
        counter=0
        validation=existing_value(data,i)
        if validation:#validacion para no ingresar a data numers repetidos
            continue
        else:
            for j in lis:
                if (j==i):
                    counter+=1
            tupla=add_two_elements_in_tupla(i,counter)
            data.append(tupla)
    return data
'''DICTIONARI FUNCTIONS'''
#filter a dictionary depending on a key and returns a list
def filter_dictionary(lis,key):
    data=[]
    for i in lis:
        for j in i.items():
            if(j[0]==key):
                data.append(j[1])
    return data
#change de value of an element in a dictionary depending of his key
def chage_value_dictionar(lis,key,to_change,new_value):
    for i in lis:
        for j in i.values():
            if j == to_change:
                index=lis.index(i)
                lis[index][key]=new_value
    return lis
#deleate de value of elements in a dictionary depending of their value
def deleate_from_dictionary(lis,value):
    for i in lis:
        for j in i.values():
            if j==value:
                index=lis.index(i)
                del lis[index]
    return lis
#search in dictionary ToF
def exist_dictionary(dictionary,to_search):
    for i in dictionary.keys():
        if i.lower()==to_search:
            return True
    return False
#return element from dictionary
def search_value_in_dictionary(dictionary,to_search):
    for i in dictionary.items():
        if i[0].lower()==to_search:
            return i[1]
#add element in dictionary
def add_element_in_dictionary(dictionary,key,value):
    dictionary.update({key:value})
    return dictionary