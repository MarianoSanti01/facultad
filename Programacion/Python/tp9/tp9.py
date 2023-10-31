#EJ1
from tp9.PersonaClass import Persona
auxname=input("Ingrese un nombre ")
auxage=int(input("Ingrese una edad "))
auxdni=input("Ingrese un documento de 9 caracteres ")
p1 = Persona(auxname,auxage,auxdni)
p1.mostrar()
p1.esMayorDeEdad()

#EJ2
from tp9.CuentaClass import Account
auxheadline=input("Ingresa el nombre del propietario de la cuenta")
auxamount=float(input("Ingresa el dinero de su cuenta. puede ser igual a 0 pero no menor "))
ac1 = Account(auxheadline,auxamount)
ac1.mostrarac
auxingreso=float(input("Ingrese dinero a su cuenta"))
ac1.ingresar(auxingreso)
auxretiro=float(input("Retire dinero de su cuenta, puede dejar la cuenta en numeros rojos (Cuidado con el veraz) "))
ac1.retirar(auxretiro)

#EJ3
from tp9.TrianguloClass import Triangle
auxside1 = float(input("Ingrese la longitud del primer lado: "))
auxside2 = float(input("Ingrese la longitud del segundo lado: "))
auxside3 = float(input("Ingrese la longitud del tercer lado: "))

t1 = Triangle(auxside1, auxside2, auxside3)

Triangle.imprimir_lado_mayor()
type = Triangle.determinar_tipo()
print(f"El triángulo es de tipo {type}")

#EJ4
from tp9.AgendaClass import Schedule
schedule = Schedule()
while True:
    print('Bienvenido al menu de tu agenda, que quieres hacer?\n[1] Añadir contacto\n[2] Lista de contactos\n[3] Buscar contacto\n[4] Editar contacto\n[5] Cerrar agenda')
    op = input('Ingresa una opción valida: ')
    if op == '1':
        print('Crear contacto\n')
        name = input('Ingresa el nombre del nuevo contacto: ')
        phone = int(input('Ingresa el telefono del nuevo contacto: '))
        gmail = input('Ingresa el gmail del nuevo contacto: ')
        schedule.add_contact(name,phone,gmail)
        print('Contacto añadido')
    elif op == '2':
        print('Ver lista de contactos')
        schedule.show_contacts()
    elif op == '3':
        to_search = input('Ingresa el nombre del contacto que quieres buscar: ')
    elif op == '4':
        to_edit = input('Ingresa el nombre del contacto que deseas editar: ')
        new_name = input('Nuevo nombre: ')
        new_phone = int(input('Nuevo teléfono: '))
        new_gmail = input('Nuevo correo electrónico: ')
        schedule.edit_contact(to_edit, new_name, new_phone, new_gmail)
        schedule.search_contacts(to_search)
    elif op == '5':
        print('Cerrando agenda')
        break
