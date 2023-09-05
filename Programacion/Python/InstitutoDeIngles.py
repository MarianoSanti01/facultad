
#Comenzamos pidiendo que coloquen una fecha con formato DIA, DD/MM
fecha = input("ingrese fecha actual colocando el día de hoy, seguido de DD/MM (numero de dia y mes) ")

#Luego tomamos cada valor por su lado, y lo colocamos en una variable
dia_sem= fecha[0:fecha.find(",")]
dia_sem= dia_sem.lower()
dia=int(fecha[fecha.find(" ")+1:fecha.find("/")])
mes=int(fecha[fecha.find("/")+1:])
lista_dias=["lunes","martes","miercoles","jueves","viernes"]

#Coloco un condicional para determinar si el día y el mes son valores validos
if(dia<31 and mes<12):

    #Dentro de este coloco otro para determinar si el nombre del dia es correcto
    if dia_sem in lista_dias:
        
        #Ahora determino la accion recomendada depende del día
        print("Actividad del día ",dia_sem, " numero ",dia, "Del mes ",mes)
        
        if dia_sem in ["lunes", "martes", "miércoles"]:
            #Lunes, martes y miércoles hay que preguntar si tomaron examenes
            tomaron_examenes = input("¿Se tomaron examenes? (Si/No): ").lower() == 'si'
            
            #Si la respuesta es sí. el programa sacara un porcentaje de alumnos aprobados
            if tomaron_examenes:            
                aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
                no_aprobados = int(input("Ingrese la cantidad de alumnos no aprobados: "))
                total_alumnos = aprobados + no_aprobados
                porcentaje_aprobados = (aprobados / total_alumnos) * 100
                print(f"Porcentaje de aprobados: {porcentaje_aprobados:.2f}%")

        elif dia_sem == "jueves":            
            #Jueves verificar si la asistencia es mayor a 50%
            asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
            if asistencia > 50:
                print("Asistio la mayoria")
            else:
                print("No asistio la mayoria")

        elif dia_sem == "viernes" and (mes == 1 or mes == 7) and dia == 1:
            #Comienzo de nuevo ciclo
            print("Comienzo de nuevo ciclo")
            alumnos_nuevo_ciclo = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel_por_alumno = float(input("Ingrese el arancel en $ por cada alumno: "))
            ingreso_total = alumnos_nuevo_ciclo * arancel_por_alumno
            print(f"Ingreso total: ${ingreso_total:.2f}")

    else:
        print("Ha ocurrido un error, intente nuevamente más tarde.")
else:
    print("Ha ocurrido un error, intente nuevamente más tarde")
