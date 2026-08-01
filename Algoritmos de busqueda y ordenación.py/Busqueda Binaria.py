"""La busqueda binaria se basa en la idea de dividir un arreglo ordenado en mitades y descartar la mitad que no contiene el elemento buscado, esto permite reducir el espacio de busqueda de manera eficiente y rapida, ya que en cada iteracion se descarta la mitad del arreglo.
La busqueda binaria tiene una complejidad temporal de O(log n) en el peor de los casos, lo que significa que el tiempo de ejecucion aumenta logaritmicamente a medida que aumenta el tamaño del arreglo, esto es mucho mas eficiente que una busqueda lineal que tiene una complejidad temporal de O(n) en el peor de los casos.
"""


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

"""otra forma"""

def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)
        
        if value == value_at_middle:
            return path_to_target, f'Value found at index {mid}'
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1
    
    return [], "Value not found"

print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))