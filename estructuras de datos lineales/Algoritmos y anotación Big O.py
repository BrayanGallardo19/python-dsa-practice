"""un algoritmo es una serie de pasos que se siguen para resolver un problema concreto, estos pueden tener cero, una o mas entradas y deben producir al menos una salida. Un algoritmo debe ser finito, es decir, debe terminar en un numero de pasos de finido y ser eficiente en el uso de recursos"""

"""a medida que el proceso crece en tamaño y complejidad, es importante mantener la eficincia para evitar un proceso lento o que incluso llegue a bloquer el sistema"""

"""Big O notation es una forma de expresar la complejidad de un algoritmo, es decir, como el tiempo de ejecución o el espacio de memoria requerido por un algoritmo crece a medida que aumenta el tamaño de la entrada, la notación Big O se utiliza para describir el peor caso de un algoritmo, es decir, el tiempo máximo que puede tardar en ejecutarse o la cantidad máxima de memoria que puede requerir"""

"""algunos ejemplos de notación Big O son:"""

"""0(1) - se conoce como complejijdad de tiempo constante, esto significa que el tiempo de ejecución del algoritmo no depende del tamaño de la entrada, es decir, siempre se ejecuta en el mismo tiempo sin importar el tamaño de la entrada """

#ejemplo

"""verificar si un numero es par o impar, este algoritmo tiene una complejidad de tiempo constante ya que solo se realiza una operacion de modulo y una comparacion, independientemente del tamaño del numero de entrada"""
def check_even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

"""0(log n) se conoce como complejidad temporal logaritmica, esto significa que el tiempo de ejecución del algoritmo aumenta levemente a medida que aumenta el tamaño de la entrada, esto es común en problemas en los que el tamaño del problema se reduce repetidamente por una fracción constante"""

"""por ejemplo binary search, este algoritmo tiene una complejidad de tiempo logaritmico ya que cada vez que se realiza una busqueda, el tamaño del problema se reduce a la mitad, es decir, se descarta la mitad de los elementos de la lista en cada iteración """

"""0(n) se conoce como complejidad temporal lineal. El tiempo de ejecución de logaritmos con esta complejidad aumenta proporcianalmnte al tamaño de la entrada"""

"""por ejemplo un ciclo for que itera sobre todo los elementos de una lista realizará mas iteraciones  a medida que aumente el numero de elementos de la lista, si la lista se duplica en tamaño, el tiempo de ejecución del ciclo for también se duplicará, por lo que la complejidad temporal es lineal"""

"""0(n log n) es conocido como complejidad temporal log lineal, esto es una complejidad temporal comun de logaritmos de ordenamiento eficientes como quicksort y mergesort"""

"""0(n^2) se conoce como complejidad temporal cuadratica, el tiempo de ejecución de estos logaritmos aumenta de forma cuadratica en relación con el tamaño de la entrada, lo cual generalmente no es eficiente para problemas del mundo real"""

"""ejemplo de estos son los bucles anidados el bucle interno realizará n iteraciones por cada una de las n iteraciones del bucle externo, resultando en n al cuadrado iteraciones """

"""otras son 0(2^n) y 0(n!) que son complejidades temporales exponenciales y factoriales respectivamente, estas son generalmente ineficientes para problemas del mundo real y se deben evitar siempre que sea posible

"""

"""https://cdn.freecodecamp.org/curriculum/lecture-transcripts/what-is-an-algorithm-and-how-does-big-o-notation-work-1.png"""


"""la notación big 0 tambien se usa para contextos de requisito de espacio, es decir, la cantidad de memoria que un algoritmo necesita para ejecutarse."""

"""los logaritmos 0(1) siempre requieren una cantidad de memoria constante incluso si su entrada crece, en contraste el espacio requerido por un algoritmo 0(n) crece proporcionalmente a medida que crece el tamaño de la entrada"""

"""y finalmente 0(n^2) requiere una cantidad de memoria que crece de forma cuadratica a medida que crece el tamaño de la entrada, un ejemplo de esto sería crear una matriz 2D donde las dimensiones se determinan por el tamao de la entrada"""