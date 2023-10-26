import random
#Escribir una función que simule el siguiente experimento: Se tiene una rata en una
#jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma
#probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5
#minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula.
#La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero
#quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
#La función debe devolver el tiempo que tarda la rata en salir de la jaula.
time=0

def experiment(timelapse):
    route=random.randint(1,3)

    if route == 1:
        timelapse += 3
    elif route == 2:
        timelapse += 5
    else:
        timelapse += 7
        return timelapse
    return experiment(timelapse)

time=experiment(time)
print(f"La rata tardó {time} minutos en salir de la jaula.")


#"Escribir una consigna apropiada para la siguiente función. Asumir que n es un número entero"
n=int(input("Ingrese un numero entero de mas de dos cifras y el programa lo dara vuelta comenzando desde el ultimo digito, con una recursion"))
def f(n):
    s=str(n)
    if len(s) <=1:
        return s
    return s[-1] + f(int(s[:-1]))
n=f(n)
print(n)
