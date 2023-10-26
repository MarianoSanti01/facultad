#Desarrollamos un codigo basandose en el comando de una nave espacial.
#primero, El codigo pedira un valor booleano para encender el motor. Con un while, que contiene un if-else con un break y un continue.
#Hasta no colocar ON, no saltara al siguiente bloque
motor = False
while motor == False:
    motor_switch = input("Para comenzar, coloque ON en la consola para prender el motor ").upper()
    if motor_switch == "ON":
        motor=True
        break
    else:
        print("Es necesario que inicie el motor para continuar")
        continue

print("Bienvenido a la nave SR. CAPITAN")
#Aquí colocamos una cantidad de tripulantes que debe ser como minimo 1 y como maximo 5, y un validador de la cantidad.
crew=0
while crew < 1 or crew >=5:
    crew = int(input("Para despegar, ingrese la cantidad de tripulantes de la nave . No pueden viajar mas de 5 personas, y al menos una "))
crew_val=0
#Colocando un while, que dice que hasta que el validador y el numero de tripulantes sean iguales, seguira repitiendo el codigo
while crew_val != crew:
    crew_val=0
    for i in range(crew):
#Colocando un FOR recorremos la cantidad de tripulantes y preguntaremos si uno por uno está listo, cuando todos estén listos, el barco arrancara
        print("Tripulante ", i+1 ,"Está listo? ")
        crew_member = input("ingrese SI o NO ").upper()
        if crew_member == "SI":
            crew_val+=1
        elif crew_member == "NO":
            print("Le recordamos que todos los tripulantes deben estar listos para zarpar, o el viaje no comenzara")
print("TODOS LOS TRIPULANTES ESTAN LISTOS; QUE TENGAN UN BUEN VIAJE!!!")