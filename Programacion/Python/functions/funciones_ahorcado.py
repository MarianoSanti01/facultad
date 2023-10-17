alphabet="abcdefghijklmnñopqrstuvwxyzáéíóú"
def verifications(letter):#verificación para que se ingrese un solo caracter y sea del alfabeto
    if (len(letter) != 1) or (letter not in alphabet) :
        print("------dato no valido ingrese una letra------")
    else:
        return True
    
def hidde_the_word(word):#funcion para tener una varible con el mismo numero de "_" que la palabra elegida
    word2=""
    for i in word:
        i="_"
        word2 += i
    return word2

def change_hidden_word(letter,word,hidden_word,guess):
    if letter in word:#si la letra ingresa en la funcion se encuentra en la palabra ingresada en la funcion
        index=0#este index indica que letras se removeran y cuales se mostraran en hidden_word
        for i in word:#el ciclo va letra por letra en la plabra
            if (i==letter):#si el valor de la iteración es igual a la letra ingresada
                lis_word=list(hidden_word)#esta variable es igual a una lista de todos los caracteres de hidden_word
                lis_word[index]=letter#se cambia la poscion indicada en el index por la letra ingresada
                hidden_word=""#hiden_word se convierte en un string vacio
                hidden_word=hidden_word.join(lis_word)#y despues se convierte en todos los carateres de lis_word
                guess +=1#aumenta el contador de ingresos
                word=word.replace(word[index],"_",1)#y la palabra elegida se le quita el caracter adivinado por si simpre se ingresa la misma letra los aciertos no suban.
            index +=1#al final de cada iteración el inedx sube en 1
        new_word=[hidden_word,guess,word]#para evitar un return de multiples valores, paso un lista con todos los valores que me interesan en mi programa principal
        print("letra correcta")
        return new_word
    else:#en caso de que la condicion no se cumpla
        new_word=[hidden_word,guess,word]#los datos de salida son iguales a los de entrada pero se imprime un mensaje indiando que la letra no es correcta
        print("letra incorrecta")
        return new_word
def final_mesagge(guess,chosen_word):#si el numero de aciertos es igual al numero de letras muestra un mensaje de victoria, cualquier otro caso uno de derrota
    if(guess==len(chosen_word)):
        return print("ganaste la pabra secreta era ",chosen_word)
    else:
        return print("perdiste la palbra secreta era ",chosen_word)

        