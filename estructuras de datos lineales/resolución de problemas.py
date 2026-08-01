"""es importante tener buenas practicas a la hora de escribir algoritmos, ya que esto puede afectar la eficiencia y la legibilidad del código.

Una buena practica es desglozar el problema y preguntarte a ti mismo 

¿cual es el objetivo del algoritmo?
¿cual es la entrada?
¿cual es la salida esperada?
¿como puedo transformar la entrada en la salida esperada?

un problema concreto sería: Invierte una cadena de caracteres 

¿Cual es la entada? una cadena de caracteres
¿cual es la salida esperada? la cadena de caracteres invertida
¿como puedo transformar la entrada en la salida esperada?

una forma de crear la idea para esa transformación y proceso es utilizar pseudocidogo que es una descripción de alto nivel de un algoritmo que es general en naturaleza y no depende de un lenguaje de programación efectivo

ejemplo:

get cadena_original

set cadena_invertida = ""

for each caracter in cadena_original:
    add caracter to the front of cadena_invertida

display cadena_invertida

algunas opciones de resolución de este problema en python son:

usar sintaxis extendida de slicing

cadena_invertida = cadena_original[::-1]

recorrer la cadena original de atras hacia adelante y agregar cada caracter a una nueva cadena

cadena_invertida = ""
for caracter in cadena_original:
    cadena_invertida = caracter + cadena_invertida

display cadena_invertida

llamar a la función reversed() y unir los caracteres en una nueva cadena
cadena_invertida = ''.join(reversed(cadena_original))

la más eficiente de estas opciones es la primera, ya que utiliza la sintaxis extendida de slicing, que es una característica incorporada de python y está optimizada para este tipo de operaciones. La segunda opción es menos eficiente ya que recorre la cadena original y agrega cada caracter a una nueva cadena, lo que puede ser costoso en términos de tiempo y memoria. La tercera opción es similar a la segunda, pero utiliza la función reversed() para invertir la cadena, lo que también puede ser menos eficiente que la primera opción.}

"""