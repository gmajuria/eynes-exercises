import math

class Circle():
    def __init__(self, radius):
        self.set_radius(radius)

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError('El radio del circulo debe ser mayor a 0')
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2
