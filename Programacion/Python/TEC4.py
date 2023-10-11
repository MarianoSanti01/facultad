from TEC4_FUNCTION import *
#EJ 1
# Inicializar listas para almacenar pasajeros y ciudades
passengers = []
cities = []

# Menú iterativo
while True:
    print("\nMenú:")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Obtener destino por DNI")
    print("4. Contar pasajeros por ciudad")
    print("5. Obtener país por DNI")
    print("6. Contar pasajeros por país")
    print("7. Salir")
    
    option = input("Seleccione una opción: ")
    
    if option == '1':
        add_passenger()
    elif option == '2':
        add_city()
    elif option == '3':
        get_destination_by_dni()
    elif option == '4':
        count_passengers_by_city()
    elif option == '5':
        get_country_by_dni()
    elif option == '6':
        count_passengers_by_country()
    elif option == '7':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")