#La funcion enumerate() devuelve un objeto enumerado que contiene pares de índice y valor de los elementos de una secuencia dada. Es útil para iterar sobre una secuencia y obtener tanto el índice como el valor de cada elemento.

#Ejemplo de uso de enumerate() con una lista
frutas = ['manzana', 'banana', 'cereza']
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

#crear una lista de tuplas con enumerate()
frutas_con_indice = list(enumerate(frutas))
print(frutas_con_indice) #[(0, 'manzana'), (1, 'banana'), (2, 'cereza')]
