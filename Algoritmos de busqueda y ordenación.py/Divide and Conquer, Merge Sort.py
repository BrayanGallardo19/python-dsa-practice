"""el paradigma divide y venceras es una tecnica de diseño de algoritmos que se basa en dividir un problema en subproblemas más pequeños y manejables, la clave de esta tecnica es la recursión, que ocurre cuando una funcion se llama a si misma repetidamente hasta que se alcanza un caso base"""

"""el logaritmo merge sort tiene tiene una complejidad temporal de 0(n log n) y una complejidad espacial de 0(n) en el peor de los casos, esto significa que el tiempo de ejecucion aumenta logaritmicamente a medida que aumenta el tamaño del arreglo y requiere una cantidad de memoria proporcional al tamaño del arreglo"""

def merge_sort(arreglo):
    if len(arreglo) <= 1:
       return arreglo
    mitad = len(arreglo) // 2
    izquierda = merge_sort(arreglo[:mitad])
    derecha = merge_sort(arreglo[mitad:])
    lista_oredanada = []
    x = 0
    y = 0
    while x < len(izquierda) and y < len(derecha):
       if izquierda[x] <= derecha[y]:
          lista_oredanada.append(izquierda[x])
          x += 1
       else:
           lista_oredanada.append(derecha[y])
           y += 1

    lista_oredanada.extend(izquierda[x:])
    lista_oredanada.extend(derecha[y:])
    return lista_oredanada
print(merge_sort([5,10,8,9,43,23,100,233,52,33,66]))