import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
circle1 = Circle(5)
print("Circle with radius:", circle1.radius)
print("Area of circle:", circle1.area())
print("Perimeter of circle:", circle1.perimeter())
print("\n3EK3_16_Saniya_Mamti")