#EJ1
def ordenamiento_burbuja_dic(diccionario):
    n = len(diccionario)
    intercambiado = True
    while intercambiado:
        intercambiado = False
        for i in range(n - 1):
            if diccionario[i]["año_publicacion"] > diccionario[i + 1]["año_publicacion"]:
                diccionario[i], diccionario[i + 1] = diccionario[i + 1], diccionario[i]
                intercambiado = True
