class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def move(self):
        print("vehicle is moving")
    
class Car(Vehicle):
    def move(self):
        print("car is driving")
    
vehicle = Vehicle("BMW", "X5")
car = Car("Toyota", "Camry")

vehicle.move()
car.move()
    
