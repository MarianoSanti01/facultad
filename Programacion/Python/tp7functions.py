#Ordenamiento burbuja
def bubble_sortdic(lista):
    n = len(lista)
    
    for i in range(n):
        # Bandera para verificar si se realizó algún intercambio en esta pasada
        intercambio_realizado = False
        
        for j in range(0, n-i-1):
            if lista[j]["año_publicacions"] > lista[j+1]["año_publicacions"]:
                # Intercambia los elementos si están en el orden incorrecto
                lista[j]["año_publicacions"], lista[j+1]["año_publicacions"] = lista[j+1]["año_publicacions"], lista[j]["año_publicacions"]
                intercambio_realizado = True
        
        # Si no se realizó ningún intercambio en esta pasada, la lista ya está ordenada
        if not intercambio_realizado:
            break
