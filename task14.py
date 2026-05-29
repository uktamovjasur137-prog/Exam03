class Calculator:
    def __init__(self, number1: float, number2: float):
        self.number1 = number1
        self.number2 = number2

    def divide(self):
        if self.number2 != 0:
            return self.number1 / self.number2
        else:
            return "0 ga bo'linmaydi"


calculate = Calculator(10, 2)

print(calculate.divide())