class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height
    def calculate_area(self):
        return 0.5 * self.base * self.height
class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)
class Parallelogram(Rectangle):
    def __init__(self, color, base, height, angle):
        super().__init__(color, base, height)
        self.angle = angle
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)
triangle = Triangle("Green", 3, 4)
square = Square("Yellow", 4)
parallelogram = Parallelogram("Purple", 5, 3, 60)

shapes = [circle, rectangle, triangle, square, parallelogram]

for shape in shapes:
    print(f"{shape.__class__.__name__} ({shape.color}): Area = {shape.calculate_area()}")
