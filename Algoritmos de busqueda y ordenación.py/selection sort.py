""""el algoritmo ordenamiento por selección funciona buscando el elemento más pequeño en la lista desordenada y cambiandolo con el elemento en la primera posición no ordenada, este comienza en la primera posición y se repite hasta que toda la lista esté ordenada su complejidad espacial es O(1) y su complejidad temporal es O(n^2)"""

def selection_sort(lista):
    if len(lista) <= 1:
        return lista

    for indice_inicial in range(len(lista) - 1):
        indice_minimo = indice_inicial
        for j in range(indice_inicial + 1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        if indice_minimo != indice_inicial:
            lista[indice_inicial], lista[indice_minimo] = lista[indice_minimo], lista[indice_inicial]

    return lista

print(selection_sort([33, 1, 89, 2, 67, 245]))
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))