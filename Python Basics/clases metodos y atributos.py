class Planet:
    def __init__(self, name, planet_type, star):
        # Verificar que todos sean strings
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")
        # Verificar que todos tengan contenido
        if name == '' or planet_type == '' or star == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')
        self.name = name
        self.planet_type = planet_type
        self.star = star
    def orbit(self):
            return f'{self.name} is orbiting around {self.star}...'
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
planet_3 = Planet("Proxima b", "Terrestrial", "Proxima Centauri")

# Imprimir objetos
print(planet_1)
print(planet_2)
print(planet_3)

# Imprimir órbitas
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())