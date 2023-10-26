#EJ3
def order_books(books, search_field):
    minor = books[0][search_field]
    index_minor=0
    for i, book in enumerate(books):
        if book[search_field] < minor:
            minor = book[search_field]
            index_minor=i
    return index_minor


#EJ5
def bubble_sortinv(lista):
    n = len(lista)
    
    for i in range(n):
        # Bandera para verificar si se realizó algún intercambio en esta pasada
        intercambio_realizado = False
        
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1]:
                # Intercambia los elementos si están en el orden incorrecto
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio_realizado = True
        
        # Si no se realizó ningún intercambio en esta pasada, la lista ya está ordenada
        if not intercambio_realizado:
            break

#Ej7
def order_nums_and_chains(list):
    nums = []
    chains =[]
    
    for element in list:
        if isinstance(element, (int,float)):
            nums.append(element)
        elif isinstance(element,str):
            chains.append(element)

    nums.sort()
    chains.sort()
    orderer_list =nums+chains
    return orderer_list