#sintaxis de un rango
#range(inicio, fin, paso)
for i in range(1, 10, 2):
    print(i) #imprime los números impares del 1 al 9

#recorrer en reversa
for i in range(10, 0, -1):
    print(i) #imprime los números del 10 al 1 en orden descendente

#crear una lista a partir de un rango
lista = list(range(1, 11))
print(lista) #imprime la lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]