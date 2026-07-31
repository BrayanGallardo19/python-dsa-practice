developer = 'Brayan'
lista = list(developer)

print(lista) 

#saber el tamaño de la lista
print(len(lista))

#saber el tipo de dato de la lista
print(type(lista))

agregar_elemento = lista.append('Hola')
print(lista)
borrar_elemento = lista.pop(0)
print(lista)

#borrar un elemento específico
lista.remove('a')
print(lista)

#buscar un elemento específico
print('y' in lista)
#listas dentro de listas
nested_list = [1, 2, [3, 4], 5]
print(nested_list[2])  # Output: [3, 4] 

usuario =['brayan',29,'data analyst']

nombre,edad,profesion = usuario
print(nombre)
print(edad)
print(profesion)

name,*resto = usuario
print(name)
print(resto)

#operador de corte
print(usuario[0:2]) #imprime los elementos desde el índice 0 hasta el índice 1 (excluyendo el índice 2)
print(usuario[:2]) #imprime los elementos desde el inicio de la lista hasta el índice
print(usuario[1:]) #imprime los elementos desde el índice 1 hasta el final de la lista

lista3 = [1, 2, 3, 4, 5,6]
print(lista3[1::2]) #imprime los elementos desde el índice 1 hasta el final de la lista, saltando de 2 en 2

#agregar un elemento a una lista
lista3.append(7)
print(lista3)
#agregar una lista a otra lista
lista4 = [8, 9, 10]
lista3.append(lista4)
print(lista3)
#extender una lista con otra lista
lista3.extend(lista4)
print(lista3)
#insertar un elemento en una posición específica
lista3.insert(0, 0)
print(lista3)
#remover un elemento específico
lista3.remove(10)
print(lista3)
#remover un elemento en una posición específica
lista3.pop(0)
#vaciar una lista
lista3.clear()

#ordenar una lista
lista5 = [3, 1, 4, 2, 5]
lista5.sort()
print(lista5)

#ordenar una lista sin modificar la lista original
lista6 = sorted(lista5)
print(lista6)

