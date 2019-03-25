class Calculator:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

calc = Calculator(30,17)

calc.add()
calc.subtract()