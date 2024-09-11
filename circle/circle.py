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

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def __mul__(self, n):
        if n <= 0:
            raise ValueError('n debe ser mayor a 0 para realizar multiplicacion')
        return Circle(self.radius * n)

    def __str__(self):
        return '----- Circulo -----\nRadio: %s' % self.radius
