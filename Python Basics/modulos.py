###Existen muchos modulos en python, ejemplo math, random, re y datetime

#math tiene funciones utiles para realizar operaciones matematicas complejas
#re se usa para trabajar con expreseiones regulares
#datetime se usa para trabajar con fechas y horas
#random es uil para generar numeros aleatorios

#para usarlos se deben importar con la sentencia impoort <nombre del modulo>

#ejemplo math

import math as m
print(m.sqrt(16))  # devuelve la raiz cuadrada de 16

#importar solo una funcion de un modulo

from math import sqrt

#tambien se les pueden asignar alias a las funciones importadas

from math import sqrt as raiz_cuadrada

from math import radians,sin,cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(f"El seno de {angle_degrees} grados es: {sine_value}")
print(f"El coseno de {angle_degrees} grados es: {cos_value}")

#por ultimo existe la declaracion * que importa todas las funciones de un modulo
#pero no es recomendable usarla porque puede causar conflictos de nombres y hace que el codigo sea menos legible


#ejemplo datetime

import datetime
birthday = datetime.date(1990, 5, 15)
print(birthday.day)
print(birthday.month)
print(birthday.year)




if__name__ == "__main__":
    print("Este código se ejecuta solo si el archivo se ejecuta directamente, no si se importa como módulo")