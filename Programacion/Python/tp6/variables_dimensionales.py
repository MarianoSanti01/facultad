#EJERCICIO 1
from funciones_dimensionales import *
from functions.numbers_addition import dni_verification
pasangers=[]
destinys=[]
while True:
    aux=[]
    print("[0 salir del programa]-[1 agregar pasajeros]-[2 agregar destino][3 ver ciudad usando el dni]")
    print("[4 ver cantidad de pasajeros ingresando una ciudad]-[5 ver pais dado un DNI][6 dado un pais mostrar cuantos pasajeros viajan]")
    choise=input()
    if(choise=="0"):
        break
    elif(choise=="1"):
        name=input("agrege el nombre del pasajero\n").lower()
        while True:
            dni=int(input("agrege el DNI del pasajero\n"))
            validation=dni_verification(int(dni))
            if(validation):
                destiny=input("ingrese destino de pasajero\n").lower()
                aux.append(destiny)
                validation1=find_tuple_in_list(destinys,aux)
                if(not validation1):
                    country=input("la ciudad ingresada no esta registrada ¿de que pais es?\n").lower()
                    data=add_two_elements_in_tupla(destiny,country)
                    destinys.append(data)
                    new_pasager=add_three_elements_in_tupla(name,dni,destiny)
                    pasangers.append(new_pasager)
                    break
                else:
                    new_pasager=add_three_elements_in_tupla(name,dni,destiny)
                    pasangers.append(new_pasager)
                    break
            else:
                print("dni invalido vuelva a ingresarlo")
    elif(choise=="2"):#verificar si ciudad existe
        new_city=input("ingrese la ciudad\n").lower()
        city_verification=existing_value(destinys,new_city)
        if city_verification:
            print("esa ciudad ya esta registrada")
        else:
            new_country=input("ingrese pais de la ciudad\n").lower()
            data=add_two_elements_in_tupla(new_city,new_country)
            destinys.append(data)
    elif(choise=="3"):
        dni=int(input("ingrese el dni del pasajero\n"))
        aux.append(dni)
        data=find_tuple_in_list(pasangers,aux)
        if data:
            city=give_element_in_tupla(pasangers,aux,2)
            print("La ciudad encontrada con el dni ingresado es ",city[0])
        else:
            print("no se encontro pasajero con ese dni")
    elif(choise=="4"):
        city=input("ingrese la ciudad para ver sus pasajeros\n").lower()
        aux.append(city)
        counter=count_in_list_tuple(pasangers,aux)
        print(counter," personas viajaran a ",aux[0])
    elif(choise=="5"):
        dni=int(input("ingrese el dni del pasajero\n"))
        aux.append(dni)
        validation2=find_tuple_in_list(pasangers,aux)
        if validation2:
            city=give_element_in_tupla(pasangers,aux,2)
            
            validation3=find_tuple_in_list(destinys,city)
            if validation3:
                country=give_element_in_tupla(destinys,city,1)
                print("el pasajero viajara a ",country[0])
            else:
                print("no se encontro la ciudad ingresada")
        else:
            print("no se encontro el dni ingresado")
    elif(choise=="6"):
        country=input("ingrese el pais para saber cuantos pasajeros viajaran\n")
        aux.append(country)
        validation4=find_tuple_in_list(destinys,aux)
        if validation4:
            city=give_element_in_tupla(destinys,aux,0)
            counter=count_in_list_tuple(pasangers,city)
            print(counter," personas viajaran a ",country)
#EJERCICIO 2
shopping=[('Nuria Costa',5,1234.5,'Calle 1 - 456'),('Nuria Costa',6,1365.5,'Calle 1 - 456'),('Jorge Russo',7,3999,'Calle 2 - 741')]
adresses=give_elements(shopping,3)
print("las direcciones de la lista son: ")
show_list(adresses)
#EJERCICIO 3
from funciones_dimensionales import *
dictionarys=[
    {"number":1,"name":'Amanda Núñez',"date":'17/03/2009',"at_day":True},
    {"number":2,"name":'Bárbara Molina',"date":'17/03/2009',"at_day":True},
    {"number":3,"name":'Lautaro Campos',"date":'17/03/2009',"at_day":True},
    {"number":4,"name":'Juan Cruz Berrios',"date":'13/03/2018',"at_day":True},
    {"number":5,"name":'Lautaro Martines',"date":'13/03/2018',"at_day":False},
    {"number":3,"name":'Billy Joel',"date":'13/03/2018',"at_day":False},
]
num_memebers=count_list(dictionarys)#numero de miembros
print("*hay ",num_memebers," ingresados")
at_day=filter_dictionary(dictionarys,"at_day")#lista con booleanos
tof=count_tof(at_day)#cantidad de socios al dia dependiendo del t o f
print("*hay ",tof[0]," socios al dia y ",tof[1]," no")
dictionarys=chage_value_dictionar(dictionarys,"date",'13/03/2018',"14/03/2018")
named=input("ingrese el nombre y apellido que eliminara\n")
dictionarys=deleate_from_dictionary(dictionarys,named)
print(dictionarys)

#Ejercicio 9

import random

def create_board(rows_, columns_):
    # Genera una lista de números para las cartas y las duplica
    numbers_ = list(range(1, (rows_ * columns_) // 2 + 1))
    cards_ = numbers_ + numbers_
    random.shuffle(cards_)
    board_ = []
    for _ in range(rows_):
        row_ = []
        for _ in range(columns_):
            card_ = cards_.pop()
            row_.append(card_)
        board_.append(row_)
    return board_

def print_board(board_, selected_):
    # Imprime el tablero de juego, ocultando las cartas no seleccionadas
    for i_ in range(len(board_)):
        for j_ in range(len(board_[i_])):
            if (i_, j_) in selected_ or board_[i_][j_] == 0:
                print(f"{board_[i_][j_]:2}", end=" ")
            else:
                print("##", end=" ")
        print()