tupla = (1, 2, 3, 4, 5)
#convertir a minusculas
tupla_minusculas = tuple(str(num).lower() for num in tupla)

diccionario = {'a': 1, 'b': 2, 'c': 3}

#eliminar un elemento del diccionario
del diccionario['b']

#validar si un diccionario está vacio
if not diccionario:
    print("El diccionario está vacío")