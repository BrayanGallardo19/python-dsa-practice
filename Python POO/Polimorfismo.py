"""El polimorfismo permite que metodos en diferentes clases compartan el mismo nombre pero realicen tareas distintas. Llamas al mismo nombre de metodo en diferentes objetos y cada uno responde a su manera"""

#ejemplo

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau"
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        return "Miau"

perro1 = Perro("Max", 3, "Labrador")
gato1 = Gato("Luna", 2, "Blanco")

print(f"Nombre: {perro1.nombre}, Edad: {perro1.edad}, Raza: {perro1.raza}, Sonido: {perro1.hacer_sonido()}")
print(f"Nombre: {gato1.nombre}, Edad: {gato1.edad}, Color: {gato1.color}, Sonido: {gato1.hacer_sonido()}")


#otro ejemplo

class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        return "Miau"
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        return "Guau"
def reproducir_sonido(animal):
    print(animal.hacer_sonido())

perro1 = Perro("Max", 3)
gato1 = Gato("Luna", 2)

reproducir_sonido(perro1)  # Salida: Guau
reproducir_sonido(gato1)   # Salida: Miau

"""el primer ejemplo es el más comun y es lo llamado polimorfismo por herencia, el segundo ejemplo es polimorfismo por duck typing, que es un concepto de python que dice que si algo camina como un pato y grazna como un pato, entonces es un pato. En este caso, no importa la clase del objeto, siempre y cuando tenga el metodo hacer_sonido()"""

