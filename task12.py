class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}. I'm {self.age}"


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        return f"My name is {self.name}. I'm {self.age}, grade: {self.grade}"


person = Person("Ali", 25)
student = Student("Jasur", 16, 8)

print(person.introduce())
print(student.introduce())


