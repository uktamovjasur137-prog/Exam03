class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"
    
animal1 = Animal("dog", "Woof")

print(animal1.make_sound())