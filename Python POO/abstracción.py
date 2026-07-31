"""la abstracción es otro principio de la programación orientada a objetos que consiste en ocultar los detalles de implementación y mostrar solo la funcionalidad escencial de un objeto, por ejemplo, a nadie que vaya a utilziar una función le interesa saber como lo hace, sino lo que hace y como hacerlo, por lo que es importante no mostrar el proceso interno sino una interfaz clara y sencilla"""

"""sumado a esto existen tambien las clases abstractas que son clases que no pueden ser instanciadas directamente y sirven como clase base, la diferencia de usar abc o no es que este se verifica en tiempo de compilación, por lo que ayuda a mantener la integridad del diseño y evitar errores involuntarios

ejemplo
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau"

perro1 = Perro("Max", 3, "Labrador")
print(f"Nombre: {perro1.nombre}, Edad: {perro1.edad}, Raza: {perro1.raza}, Sonido: {perro1.hacer_sonido()}")    

"""basicamente aquí lo que hacemos con @abstractmethod es oblgiar a la clase perro a sobreescribir el metodo hacer_sonido() con esto evitamos que al crear una clase derivada de Animal el metodo hacer_sonido() no tenga un sentido logico y nos ayude a mantener la integridad del diseño y evitar errores involuntarios ya que si no mantendría el comportamiento de la clase base"""


