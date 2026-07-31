""" La programación orientada a objetos o OOP (Object-Oriented Programming) es un estilo de programación en el que se trata el codigo como un objeto de la vida real 

ejemplo

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad   

        def saludar(self):
            print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Juan", 30)

en este caso tenemos el objeto persona1 que es una instancia de la clase Persona, y tiene atributos nombre y edad, y un método saludar() que imprime un mensaje de saludo.

tal cual como si fuera una persona real

la POO tiene 4 principios fundamentales que te ayudan a organizar y gestionar el codigo de manera más eficiente y modular. Estos principios son:

encapsulación, herencia, polimorfismo y abstracción.

encapsulación: es la agrupación de los atributos y metodos de un objeto en una sola unidad, la clase.

con la encapsulación puedes ocultar el estado interno del objeto detras de un conjunto simple de metodos y atributos publicos que actual como puertas. Detras de esas puertas estásn los atributos y metodos privados que no pueden ser accedidos directamente desde fuera de la clase. Esto ayuda a proteger el estado interno del objeto y a mantener la integridad de los datos.


ejemplo de encapsulación
"""
class Wallet:
   def __init__(self, balance):
       self._balance = balance # For internal use by convention

   def deposit(self, amount):
       if amount > 0:
           self._balance += amount # Add to the balance safely

   def withdraw(self, amount):
       if 0 < amount <= self._balance:
           self._balance -= amount # Remove from the balance safely

"""anteponer un guion bajo (_) al nombre de un atributo o método indica que es privado y no debería ser accedido directamente desde fuera de la clase. Esto es solo una convención y no impide el acceso, pero ayuda a los desarrolladores a entender que esos elementos son internos y no forman parte de la interfaz pública de la clase."""

"""mientras que anteponer dos guiones bajos (__) al nombre de un atributo o método activa el name mangling, que es una técnica que cambia el nombre del atributo o método para hacerlo más difícil de acceder desde fuera de la clase. Esto proporciona un nivel adicional de protección y ayuda a evitar conflictos de nombres en clases derivadas."""