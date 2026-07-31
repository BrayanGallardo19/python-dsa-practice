class Animal:
    def __init__(self, nombre,edad):
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
perro1 = Perro("Max", 3, "Labrador")
print(f"Nombre: {perro1.nombre}, Edad: {perro1.edad}, Raza: {perro1.raza}, Sonido: {perro1.hacer_sonido()}")