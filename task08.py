class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
rectangle1 = Rectangle(5, 10)

print(rectangle1.area())