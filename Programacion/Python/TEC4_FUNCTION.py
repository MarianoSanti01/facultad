#EJ1
# Función para agregar pasajeros a la lista de viajeros
def add_passenger(passengers):
    name = input("Ingrese el nombre del pasajero: ")
    dni = int(input("Ingrese el DNI del pasajero: "))
    destination = input("Ingrese el destino del pasajero: ")
    passengers.append((name, dni, destination))

# Función para agregar ciudades a la lista de ciudades
def add_city(cities):
    city = input("Ingrese el nombre de la ciudad: ")
    country = input("Ingrese el país al que pertenece la ciudad: ")
    cities.append((city, country))

# Función para obtener el destino de un pasajero por DNI
def get_destination_by_dni(passengers):
    dni = int(input("Ingrese el DNI del pasajero: "))
    for passenger in passengers:
        if passenger[1] == dni:
            print(f"El pasajero {passenger[0]} viaja a {passenger[2]}")
            return
    print("Pasajero no encontrado.")

# Función para contar pasajeros que viajan a una ciudad
def count_passengers_by_city(passengers):
    city = input("Ingrese el nombre de la ciudad: ")
    count = sum(1 for passenger in passengers if passenger[2] == city)
    print(f"La cantidad de pasajeros que viajan a {city} es: {count}")

# Función para obtener el país de destino de un pasajero por DNI
def get_country_by_dni(passengers,cities):
    dni = int(input("Ingrese el DNI del pasajero: "))
    for passenger in passengers:
        if passenger[1] == dni:
            for city, country in cities:
                if city == passenger[2]:
                    print(f"El pasajero {passenger[0]} viaja a {country}")
                    return
    print("Pasajero no encontrado.")

# Función para contar pasajeros que viajan a un país
def count_passengers_by_country(passengers,cities):
    country = input("Ingrese el nombre del país: ")
    count = sum(1 for passenger in passengers for city, c in cities if city == passenger[2] and c == country)
    print(f"La cantidad de pasajeros que viajan a {country} es: {count}")

#EJ2
