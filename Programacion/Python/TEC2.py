#EJERCICIO 1

corrimiento = int(input("Ingrese la cantidad de valores que se correra su frase "))
abece="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

for i in range(5):
    frase= input("Ingrese una frase ").upper()
    frase_enc= ""
    for letra in frase:
        if letra in abece:
            indice = abece.find(letra) 
            indice= (indice+corrimiento)%27
            frase_enc += abece[indice]
            
        else:
            frase_enc +=letra
    print(frase_enc)

print("__________________________________________________")
#EJERCICIO 2

numero=1
partotal=0
impartotal=0
while numero != "0":
    numero = input("Ingrese una cifra para desglozarla ")
    par=0
    impar=0
    for i in numero:
        cifra = int(i)
        if (cifra%2==0) :
            par= par+1
            partotal=partotal+1
        else:
            impar= impar+1
            impartotal=impartotal+1
    print("Sus numeros pares son ", par, " Sus numeros impares son ",impar)
print("La totalidad de sus numeros pares es ",partotal, ". Mientras que la totalidad de sus impares es ", impartotal)
