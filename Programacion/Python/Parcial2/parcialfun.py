def is_mutant(adn):
    #Funcion que busca los 4 valores iguales
    def check_sequence(sequence):
        #Busca la igualdad, comparando los valores obtenidos del teclado con modelos de secuencia.
        if "AAAA" in sequence or "TTTT" in sequence or "CCCC" in sequence or"GGGG" in sequence:
            return True
        return False
    isamutant=0

#Busqueda horizontal
    for row in adn:
        if check_sequence(row):
            isamutant+=1


#Busqueda vertical
#Une todos los valores de las filas que se encuentren en la misma columna mediante el join, y los compara con el checker
    for col in range(6):
        col_sequence =''.join(adn[row][col]for row in range(6))
        if check_sequence(col_sequence):
            isamutant+=1


#Busqueda diagonal de izquierda HACIA ABAJO
#Toma un valor y busca la diagonal de este con un for auxiliar que va sumandole un valor por cada vuelta. a diferencia de los anteriores este solo toma 4 valores y solo en el rango que puedan existir 4 o mas valores, en este caso, del 1 al 3.
    for row in range(3):
        for col in range(3):
            diagonal = ''.join(adn[row+i][col+i] for i in range(4))
            if check_sequence(diagonal):
                isamutant+=1


#Toma un valor y busca la diagonal de este con un for auxiliar que va sumandole un valor por cada vuelta a las filas, pero a las columnas se las resta. a diferencia del anterior, el rango de columnas pasa de ser de 1 a 3, a ser de 3 a 6
#Busqueda diagonal de derecha HACIA ABAJO
    for row in range(3):
        for col in range(3, 6):
            diagonal = ''.join(adn[row+i][col-i] for i in range(4))
            if check_sequence(diagonal):
                isamutant+=1

#Todas las comprobaciones arrojan un +1 a isamutant, para cumplir la condicion de dos o más lineas
    if isamutant >= 2:
        return True
#Si no encuentra coincidencias el bucle regresa con valor false
    return False