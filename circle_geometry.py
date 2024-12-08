class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"area of cirlcle is {3.14 * self.radius * self.radius}")
    def perimeter(self):
        print(f"perimeter of circle is {3.14 * 2 * self.radius}")
s=circle(5)
s.area()
s.perimeter()
