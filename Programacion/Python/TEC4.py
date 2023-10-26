from TEC4_FUNCTION import *
#EJ 1
passengers_list=[]
passengers_destiny=[]

#passenger= ('Name','DNI','province_destiny')
def add_passengers():
    print("Ingresa nombre, DNI, Destino")
    name= input("Ingresa el nombre y apellido ")
    dni= input("Ingresa su documento ")
    destiny= input("Ingresa el destino del pasajero ")
    passenger=(name,dni,destiny)
    passengers_list.append(passenger)

def add_citys():
    name_city= input("Ingresa el nombre de la ciudad")
    name_country= input("ingrese el pais ")
    city=(name_city,name_country)
    passengers_destiny.append(city)

def dni_city():
    exist=False
    dni = input("Ingresa el documento que desea buscar")
    for passenger in passengers_list:
        if passenger[1] == dni:
            print(f'El pasajero de DNI {dni} viajara a {passengers_list[2]}')
            exist = True
        if exist != True:
            print("El pasajero no fue encontrado")

def city_cuantity():
    counter=0
    city_to_search = input("Ingrese la ciudad a buscar")
    for passenger in passengers_list:
        if passenger[2] == city_to_search:
            counter+=1
    print(f'viajaran {counter} pasajeros a {city_to_search}')
#Menú interactivo

def dni_country():
    

while(True):
    print('[1] Agregar pasajeros a la lista de viajeros \n [2] Agregar ciudades a la lista de ciudades \n[3]ver ciudad destino con DNI\n[4]Dada una ciudad mostrar cantidad de pasajeros\n[5]Dado un DNI ver a que país viaja\n[6]Dado un pais, mostrar cuantos pasajeros viajan a ese pais\n[7]Salir')
    op= int(input("Selecciona una opcion valida"))
    if op ==1:
        add_passengers()
    elif op ==2:
        add_citys()
    elif op ==3:
        dni_city()
    elif op ==4:
        city_cuantity()

