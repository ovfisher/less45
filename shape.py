class Shape():
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
#self.radius — это характеристика, а radius — переменная, которая будет свое значение передавать в эту характеристику.
    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Square(Shape):
    def __init__(self, width):
        self.width = width
    def area(self):
        return self.width ** 2

def print_area(shape):
    print(f"Площадь - {shape.area()}")

circle = Circle(5)
square = Square(7)

print_area(circle)
print_area(square)

