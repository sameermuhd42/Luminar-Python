class Animal:
    def __int__(self, age):
        self.age = age

    def printval(self):
        print("Age:", self.age)


class Dog(Animal):
    def __init__(self, color):
        super.__init__()
        self.color = color

    def print_value(self):
        print("Color:", self.color)


d1 = Dog(6, "Brown")
d1.printval()
d1.print_value()