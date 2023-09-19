#Realizar un programa que cumpla con las siguientes condiciones:

#edir al usuario su nombre. Cada vez que el programa interactúe con él debe llamarlo por su nombre.
#Generar un menú de opciones, que serán:
#Juego de números.
#Juego de palabras.
#Si el usuario elige la primera opción, se debe pedir el ingreso de números enteros (condición de salida: cuando ingrese 0). Al finalizar mostrar por pantalla:
#El mayor número par.
#El promedio de los números impares.
#Si el usuario elige la segunda opción, se debe pedir el ingreso de una frase y mostrar por pantalla la cantidad de cada vocal que contiene dicha frase.
#No olvides realizar las debidas validaciones!


#Cominenzo dandole un nombre al usuario.
name= input("Hola! ingrese su nombre ").capitalize()
print("Perfecto ",name, "Qué desea jugar?")
#Pregunto qué desea jugar y con un while, lo mantengo adentro del menu hasta que seleccione una opcion, con SALIR el codigo se cierra.
option=" "
while option == " ":
    option= input(f"Ingrese A para jugar a un juego de numeros. y B para jugar a un juego de palabras,o SALIR para salir. {name} ").upper()
    if option == "A":
        #Defino todos los valores. Num= al numero que se pedira. pair = numeros pares. cuantity= son todos los numeros que ingresare, exceptuando 0 y negativos
        #odd son los numeros impares.
        print(f"Perfecto {name}, usted a decidido jugar a un juego de numeros. Ingrese numeros enteros . El programa le dirá cual fue el mayor numero par, y el promedio de los numeros impares")
        num= 1
        pair=0
        cuantity=0
        odd=0
        #mientras el numero sea distinto a 0 el programa correra.
        while num != 0 :
            num= (input(f"ingrese un numero {name} Recuerde que el 0 debe ser para salir "))
            #si el numero es mayor a cero, buscara los numeros pares, y reemplazara el par guardado que por defecto es 0
            #Al ser impar, lo añadira a una lista de impares que luego sacara el porcentaje de numeros impares en el total de numeros
            #Al ser un numero menor a 0 dara error, y volverá al programa nuevamente.
            #Al ser 0 imprimirá todo lo que hizo mientras el numero no era 0
            if num.isdigit():
                num=int(num)
                if num > 0:
                    cuantity=cuantity+1
                    if num%2==0:
                        if num>pair:
                            pair=num
                    elif num%2!=0:
                        odd=odd+1
                elif num == 0:
                    print(f"hasta la proxima,{name} ")
                    print(f"{name}, Su numero par mayor fue {pair}")
                    print(f"{name}, usted ingresó {cuantity} numeros, de los cuales ", (odd/cuantity)*100," %", " de los numeros es impar" )
                    break
                else:
                    print("Numero invalido")
                    continue
    elif option =="B":
        #Se pide una palabra, y se la pasa a minuscula para validar correctamente
        print(f"Perfecto {name} usted decidio jugar con palabras. ingrese una palabra y el programa le dira cuantas de cada vocales tiene")
        phrase=input().lower()
        a=0
        e=0
        i=0
        o=0
        u=0
        #añadiendo un contador de cada letra, se irá sumando cada una a su respectivo lugar. con el for recorreremos la frase y con if y elif, sumaremos las vocales
        for letter in phrase:  
            if letter == "a":
                a += 1
            elif letter == "e":
                e += 1
            elif letter == "i":
                i += 1
            elif letter == "o":
                o += 1
            elif letter == "u":
                u +=1
        print(f"{name}, usted ingreso un total de {a} veces la letra A")
        print(f"{name}, usted ingreso un total de {e} veces la letra E")
        print(f"{name}, usted ingreso un total de {i} veces la letra I")
        print(f"{name}, usted ingreso un total de {o} veces la letra O")
        print(f"{name}, usted ingreso un total de {u} veces la letra U")
    elif option =="SALIR":
        print(f"Hasta la proxima, {name} ")
        break
    else:
        option=" "
        continue