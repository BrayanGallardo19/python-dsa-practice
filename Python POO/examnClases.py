import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        cadena = ""
        for _ in range(self.height):
            cadena += '*' * self.width + '\n'
        return cadena

    def get_amount_inside(self, figura):
        return (self.width // figura.width) * (self.height // figura.height)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width

    def set_height(self, new_height):
        self.width = new_height
        self.height = new_height

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    def __str__(self):
        return f'Square(side={self.width})'