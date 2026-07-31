#las clases son moldes o plantillas que nos permiten definir comportamientos compartidos luego creas objetos que usan esos comportamientos

#para crear una clase se usa la palabra clave class seguido del nombre de la clase y dos puntos.Luego, dentro de la clase, puedes agregar un inicializador junto con cualquier atributo y metodo

#Los atributos son variables dentro de una clase y se usan para almacenar información sobre el objeto. Los metodos son funciones definidas dentro de una clase y son las acciones que los objetos creados con una clase pueden realizar.

#sintaxis

class NombreDeLaClase:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sample_method(self):
        print(self.name.upper)

#def __init__ es el metodo especial que se llama automaticamente cuando se crea un objeto de la clase, se usa para inicializar los atributos del objeto, es el metodo constructor de la clase.

#ademas de esos __init__ siempre es una referencia al objeto especifico que se esta creando. Por convención este parametro se llama self pero puedes usar cualquier nombre, pero es recomendable seguir la convención para mantener la claridad del código.

#self.name = name y self.age son lo atributos que tendrán los objetos

#def sample_metohd(self) es un metodo de la clase que puede acceder a los atributos del objeto usando self. En este caso, sample_method imprime el nombre del objeto en mayúsculas.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof!")

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.bark()  # Output: BUDDY says woof woof!
dog2.bark()  # Output: MAX says woof woof!

# METODOS Y ATRIBUTOS 

#EXISTEN DOS TIPOS DE ATRIBUTOS: DE INSTANCIA Y DE CLASE

#LA DIFERENCIA PRINCIPAL ES QUE LOS ATRIBUTOS DE CLASE SON COMPARTIDOS POR TODAS LAS INSTANCIAS (OBJETOS) Y SE DEFINEN FUERA DEL METODO __Init__ mientras que los atributos de instancia son especificos de cada objeto y se definen dentro del metodo __init__ (constructor)

class Dogs:
    species = 'French Bulldog' # atributo de clase

    def __init__(self, name): # atributo de instancia
        self.name = name

print(Dogs.species)  # Output: French Bulldog
dog1 = Dogs("Buddy")
print(dog1.name)  # Output: Buddy
print(dog1.species)  # Output: French Bulldog


# Metodos especiales, magicos o dunder

#son metodos especiales de python que comienzan y terminan con dobles guiones bajos __, la palabra dunder proviene de dobles guiones bajos.

#hay varios metodos especiales como __add__, __init__, __len__, __str__ entre otros 

#normalmente no los utilizas directamente sino que se invocan de manera implicita a traves de operadores o funciones integradas de python.

#como cuando haces una suma de dos objetos, python invoca el metodo __add__ de la clase del objeto, o cuando llamas a len(objeto) python invoca el metodo __len__ de la clase del objeto.

#cuando creas tu propia clase python no sabrá como manejar las cosas automaticamente, aqui es donde entran los metodos especiales, te permiten personalizar el comportamiento incorporado de python

#digamos que quieres obtener el numero de paginas de un objeto libro  o compararlos y obtener una cadena legible de los objetos

#esto es lo que pasa si lo metodos no están definidos

class Book:
   def __init__(self, title, pages):
       self.title = title
       self.pages = pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1)) # TypeError: object of type 'Book' has no len()
print(str(book1)) # <__main__.Book object at 0x102ed2900>
print(book1 == book2) # False even though they have the same number of pages

# a continuación como se ppueden definir

class Book:
    def __init__ (self, title, pages):
        self.title = title
        self.pages = pages
    def __len__(self):
        return self.pages
    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.pages == other.pages
        return False

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1))  # Output: 420
print(str(book1))  # Output: Book: Built Wealth Like a Boss, Pages: 420
print(book1 == book2)  # Output: True

#otro ejemplo con carrito de compra.

class Cart:
   def __init__(self):
       self.items = []

   def add(self, item):
       self.items.append(item)

   def remove(self, item):
       if item in self.items:
           self.items.remove(item)
       else:
           print(f'{item} is not in cart')

   def list_items(self):
       return self.items

   def __len__(self):
       return len(self.items)

   def __getitem__(self, index):
       return self.items[index]

   def __contains__(self, item):
       return item in self.items

   def __iter__(self):
       return iter(self.items)