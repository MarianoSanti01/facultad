from parcialfun import *
#PRUEBA CON UNA LINEA VERTICAL(AAAA) Y UNA HORIZONTAL(TTTT)
"GTGTTG"
"ACGCGC"
"AGTTTG"
"ATTTTC"
"ACGCGT"
"GGCAGT"
#PRUEBA DE AMBAS DIAGONALES (GGGG)(CCCC)
"ATAATC"
"TATACT"
"ATGCTA"
"TACGAT"
"CGTTGC"
"TCAATG"
#PRUEBA NO MUTANTE
"TATATA"
"GCGCGC"
"TATATA"
"GCGCGC"
"TATATA"
"GCGCGC"
exit_=False
print("Bienvenido a Magnus Lab, ingrese a su sujeto en la maquina de pruebas para determinar si es mutante. ")
#Al final de cada muestra de ADN, el programa preguntara si deseas salir.
while not exit_:
    adn=[]
    print("Ingrese una por una las filas de ADN, con todas las letras juntas. ATGC son los unicos valores permitidos")
    for i in range(6):
        fileval=False
        while not fileval:
            row=""
            row=input(f" Fila {i+1}: ").upper()
            if len(row) != 6 or not all(base in "ATCG" for base in row):
                print("La fila debe tener solo 6 letras y las unicas que están admitidas son A,T,G,C")
            else:
                adn.append(row)
                fileval=True
#Una vez que termina el bucle for que señaliza cuantas filas quedan por depositar, se corre la funcion
    isornot=is_mutant(adn)
#En base al valor booleano, devuelve una respuesta. y pregunta si quieren hacerlo de nuevo
    if isornot==True:
        print("Felicidades, su sujeto pasó la prueba y su ADN coincide con los fenotipos, es un mutante")
    else:
        print("Lo lamentamos, su sujeto no pasó la prueba... Y está muerto")
    exitv=""
    while exitv != "SI" and exitv != "NO":
        exitv=input("¿Desea intentar nuevamente con otro sujeto? Si/No ").upper()
        if exitv=="NO":
            exit_=True
            print("Gracias por usar la Mutanteando 3000, Adios!")
        elif exitv=="Si":
            print("Usted es un monstruo")