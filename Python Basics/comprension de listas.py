#comprensiones de listas
#La sintaxis de una comprensión de lista es: [expresión for elemento in iterable if condición]

#ejemplo

numerosjustos = [numero for numero in range(1, 11) if numero % 2 == 0]
print(numerosjustos) #imprime [2, 4, 6, 8, 10]
#esto se interpreta como: para cada numero en el rango del 1 al 10, si el numero es divisible por 2, entonces se agrega a la lista numerosjustos, el primer numero significa el valor que se va a agregar a la lista, el segundo numero es el elemento que se va a iterar, el tercer numero es la condición que se debe cumplir para agregar el elemento a la lista

lista = ['a', 'b', 'c', 'd', 'e']
#crear una nueva lista con mayusculas usando comprension de listas
mayusculas = [letra.upper() for letra in lista]
print(mayusculas) #imprime ['A', 'B', 'C', 'D', 'E']

numbers = [1, 2, 3, 4, 5]
result = [(num,'even') if num % 2 == 0 else (num,'odd') for num in numbers ]
print(result) #imprime [(1, 'odd'), (2, 'even'), (3, 'odd'), (4, 'even'), (5, 'odd')]
#interpretacion: para cada num en la lista numbers, si num es divisible por 2, entonces se agrega una tupla (num,'even') a la lista result, de lo contrario se agrega una tupla (num,'odd') a la lista result


lista = [1,2,3,4,5,6]

resultado = [num*2 for num in lista]
print(resultado) #imprime [2, 4, 6, 8, 10, 12]


#filter() es una función incorporada en Python que se utiliza para filtrar elementos de una secuencia (como una lista) según una función de filtrado que devuelve True o False. La sintaxis de filter() es: filter(función, iterable)

listas = ['ana', 'oso', 'python', 'radar', 'java']
def es_palindromo(palabra):
    return palabra == palabra[::-1]
palindromos = list(filter(es_palindromo, listas))
print(palindromos) 


#funcion map() es una función incorporada en Python que se utiliza para aplicar una función a cada elemento de una secuencia (como una lista) y devolver un nuevo iterable con los resultados. La sintaxis de map() es: map(función, iterable)
numeros = [1, 2, 3, 4, 5]
def cuadrado(num):
    return num ** 2 
cuadrados = list(map(cuadrado, numeros))
print(cuadrados) #imprime [1, 4, 9, 16, 25] 