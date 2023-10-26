#Ordenamiento burbuja
def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n):
        # Bandera para verificar si se realizó algún intercambio en esta pasada
        intercambio_realizado = False
        
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Intercambia los elementos si están en el orden incorrecto
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio_realizado = True
        
        # Si no se realizó ningún intercambio en esta pasada, la lista ya está ordenada
        if not intercambio_realizado:
            break

#Selection sort
def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        # Encuentra el índice del elemento mínimo en el resto de la lista
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        # Intercambia el elemento actual con el elemento mínimo encontrado
        lista[i], lista[min_index] = lista[min_index], lista[i]

#Insertion sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        # Guarda el valor actual a ser insertado en su posición correcta
        valor_actual = lista[i]
        j = i - 1
        
        # Desplaza los elementos mayores que el valor actual a la derecha
        while j >= 0 and len(valor_actual) < len(lista[j]):
            lista[j + 1] = lista[j]
            j -= 1
        
        # Inserta el valor actual en su posición correcta
        lista[j + 1] = valor_actual

#Merge sort
def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        # Fusiona las dos sublistas
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Verifica si quedan elementos sin fusionar en ambas sublistas
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

#Ordenamiento por conteo
def counting_sort(arr):
    max_val = max(arr)  # Encontrar el valor máximo en la lista
    count = [0] * (max_val + 1)  # Crear una lista de conteo
    sorted_arr = [0] * len(arr)  # Crear una lista para el resultado
    # Contar las ocurrencias de cada valor
    for num in arr:
        count[num] += 1
    # Llenar la lista ordenada basada en el conteo
    index = 0
    for i in range(len(count)):
        for _ in range(count[i]):
            sorted_arr[index] = i
            index += 1
    return sorted_arr




#Busqueda Lineal
def busqueda_lineal(lista, elemento_buscado):
    for i, elemento in enumerate(lista):
        if elemento == elemento_buscado:
            return i  # Devuelve el índice del elemento si se encuentra
    return -1  # Devuelve -1 si el elemento no se encuentra en la lista

#Busqueda binaria
def busqueda_binaria(lista, elemento_buscado):
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == elemento_buscado:
            return medio  # Elemento encontrado, devuelve el índice.
        elif lista[medio] < elemento_buscado:
            izquierda = medio + 1  # El elemento buscado está en la mitad derecha.
        else:
            derecha = medio - 1  # El elemento buscado está en la mitad izquierda.
    return -1  # Elemento no encontrado.

