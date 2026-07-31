#funcion zip

#La función zip() toma iterables (pueden ser cero o más), los agrupa en tuplas y devuelve un iterador de tuplas. Cada tupla contiene elementos de los iterables correspondientes en la misma posición. La función zip() se detiene cuando el iterable más corto se ha agotado.

#Ejemplo de uso de zip() con dos listas
nombres = ['Alice', 'Bob', 'Charlie']
edades = [25, 30, 35]
combinados = zip(nombres, edades)
print(list(combinados)) # [('Alice', 25), ('Bob', 30),

#recorrer los elementos combinados con zip()
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

#recorrer ya combinados
combinados = zip(nombres, edades)
for combinado in combinados:
    for elemento in combinado:
        print(elemento) #imprime cada elemento de las tuplas combinadas por separado