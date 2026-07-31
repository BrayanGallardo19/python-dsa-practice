mi_set = {1, 2, 3, 4, 5}
otro_set = {4, 5, 6, 7, 8, 9}

#verifica si los conjuntos tienen elementos en común
print(mi_set.isdisjoint(otro_set))  # {1, 2, 3, 4, 5}
#devuelve la unión de los conjuntos
print(mi_set.intersection(otro_set))  # {4, 5}
#devuelve los elementos que están en mi_set pero no en otro_set
print(mi_set.difference(otro_set))  # {1, 2, 3}

#issubset verifica si un conjunto es un subconjunto de otro
#para que sea True, todos los elementos del conjunto deben estar en el otro conjunto
print(mi_set.issubset(otro_set))  # False porque mi_set tiene elementos que no están en otro_set
print(otro_set.issubset(mi_set))  # False porque otro_set tiene elementos que no están en mi_set
#issuperset verifica si un conjunto es un superconjunto de otro
#para que sea True, el conjunto debe contener todos los elementos del otro conjunto
print(mi_set.issuperset(otro_set))  # False porque otro_set tiene elementos que no están en mi_set
print(otro_set.issuperset(mi_set))  # False porque otro_set tiene elementos que no están en mi_set


#Operadores de conjuntos
#Operador | devuelve la unión de dos conjuntos
print(mi_set | otro_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
#Operador & devuelve la intersección de dos conjuntos
print(mi_set & otro_set)  # {4, 5}
#Operador - devuelve la diferencia de dos conjuntos
print(mi_set - otro_set)  # {1, 2, 3}
#Operador ^ devuelve la diferencia simétrica de dos conjuntos (elementos que están en uno de los conjuntos pero no en ambos)
print(mi_set ^ otro_set)  # {1, 2, 3, 6, 7, 8, 9}
