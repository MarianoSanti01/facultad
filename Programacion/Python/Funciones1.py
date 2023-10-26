#DEFINICIÓN DE FUNCIONES
#Cambie los valores dentro de la funcion, pues deben tener el mismo valor declarado en el nombre
def most(a,b): 
    if(a>b):
        return a
    else:
        return b
def least (a,b):
    if(a<b):
        return a
    else:
        return b

#PROGRAMA PRINCIPAL

x= int(input('Un número: ')) 
y= int(input('Otro número: '))

print(most(x-3, least (x+2, y-5)))