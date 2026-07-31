"""Los getters son metodos y setters son  metodos que permiten controlar como se accede y modifican los atributos de una clase. Con los getters obtienes un valor y con los setters puedes establecer un valor

esta acción se realiza a traves de lo que se conoce como propiedades que son lo que conecta los atributos privados con los metodos publicos que permiten acceder a ellos de manera controlada.

las propiedades actuan como atributos pero se comportan como metodos internamente, esto significa que puedes que puedes acceder a las propiedades con notación de punto como si fueran atributos normales, pero en realidad se ejecutan los metodos getter y setter asociados a ellas.

ejemplo de getter y setter

"""

class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute

    @property
    def radius(self):
        return self.__radius

    @property
    def area(self):
        return 3.14159 * self.__radius ** 2

    @radius.setter
    def radius(self,value):
        if value < 0:
            raise ValueError("El valor no puede ser negativo")
        self.__radius = value

"""nota clave, en el metodo setter no puedes usar el mismo nombre del atributo privado que estas tratando de modificar, ya que esto generaria una recursión infinita. En su lugar, debes usar un nombre diferente para el parametro del metodo setter, como se muestra en el ejemplo con 'value'.
"""

my_circle = Circle(5)

print(my_circle.radius)  # Output: 5
print(my_circle.area)    # Output: 78.53975
print(my_circle.radius)  # Output: 5    
my_circle.radius = 10
print(my_circle.radius)  # Output: 10


class Persona:
    def __init__(self,rut,nombre,apellido):
        self.__rut = rut
        self.__nombre = nombre
        self.apellido = apellido

    @property
    def rut(self):
        return self.__rut

persona1 = Persona("12345678-9","Juan","Perez")
print(persona1.rut)  # Output: 12345678-9
persona1.__nombre = "Pedro"  # This will not change the private attribute
print(persona1.__nombre)  # Output: Pedro (this is a new attribute, not the private one)
print(persona1._Persona__nombre)  # Output: Juan (accessing the private attribute using name mangling)
persona1._Persona__nombre = "Pedro"  # This will change the private attribute
print(persona1._Persona__nombre)  # Output: Pedro (the private attribute has been changed)



"""deleter"""

class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute

    @property
    def radius(self):
        return self.__radius

    @property
    def area(self):
        return 3.14159 * self.__radius ** 2

    @radius.setter
    def radius(self,value):
        if value < 0:
            raise ValueError("El valor no puede ser negativo")
        self.__radius = value

    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self.__radius

my_circle2 = Circle(5)
del my_circle2.radius 
try:
    print(my_circle2.radius)  # This will raise an AttributeError since the radius has been deleted
except AttributeError as e:
    print(f"Error: {e}")  # Output: Error: 'Circle' object has no attribute '_Circle__radius' 