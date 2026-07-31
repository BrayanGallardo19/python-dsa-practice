#aveces puede que no sepas que atributos necesitas hasta que tu programa esté en ejecución

#imagina que estás escribiendo un script que recibe nombres de atirbutos de un usuario o de un archivo de configuración. Esos no son atributos que puedas codificar de maneera fija o con anticipación

#Ahí es donde entra el manejo dinamico, de esta manera puedes acceder, modificar, verificar o eliminar atributos usando sus nombres como variables

#pyrhon ofrece cuatro funciones integradas para manjar atributos de objetos. Son getattr(), setattr(), hasattr() y delattr()

#getattr hace posibles leer un atributo de un objeto cuando no conoces su nomnbre hasta el tiempo de ejecución, si este no existe genera un AttributeError pero puedes proporcionar un valor por defecto para evitar el error

#para usarlo pasa el objeto, el nombre del atributo y un valor predeterminado opcional

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person = Person("Alice", 30)

print(getattr(person, "name"))  # Output: Alice
print(getattr(person, "age"))  # Output: 30
print(getattr(person, "gender", "Not specified"))  # Output: Not specified

#aqui el atributo genero no existe por lo que se devuelve el valor predeterminado "No especificado" en lugar de generar un error

#ademasa puede que quieras revisar todos los atributos que tiene un objeto, no solo los que ya conoces. La función dir te lo permite. devuelve una lista de todos los atributos y métodos de un objeto, incluidos los heredados de su clase base. Esto es útil para inspeccionar objetos y descubrir qué atributos están disponibles para su uso.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

#Bucle para imprimir todos los atributos y métodos del objeto person
for attribute in dir(person):
    print(attribute) # Output: age, name, __init__, __str__, etc. (including inherited attributes and methods)

for attribute in dir(person):
    if not attribute.startswith('__') and not callable(getattr(person, attribute)): 
        value = getattr(person, attribute)
        print(f"{attribute}: {value}") # Output: name: Alice, age: 30
#otro ejemplo de configuración

class Configuration:
    pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Dynamically set attributes using dictionary keys and values
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) # https://api.example.com
print(config_obj.timeout_sec) # 30

#tambien existe hasattr() que permite verificar si un objeto tiene un atributo específico. Devuelve True si el atributo existe y False en caso contrario.

#sintaxis basica hasattr(objeto, nombre_atributo)

#ejemplo

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
product = Product("Laptop", 1200)

atributos = ["name", "price", "stock"]
for attr in atributos:
    if hasattr(product, attr):
        print(f"{attr} exists with value: {getattr(product, attr)}")
    else:
        print(f"{attr} does not exist.")

#finalmente existe delattr() que permite eliminar un atributo de un objeto. Si el atributo no existe, se genera un AttributeError, es util por ejemplo para eliminar todos los atributos de un objeto que ya no son necesarios o para limpiar un objeto antes de reutilizarlo.

#ejemplo

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

user = User("john_doe", "john@example.com")

print(f"Before deletion: username = {user.username}, email = {user.email}")

delattr(user, "email")

print(f"After deletion: username = {user.username}, email = {user.email}")

