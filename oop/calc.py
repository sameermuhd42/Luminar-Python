class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def printval(self):
        add = self.num1 + self.num2
        sub = self.num1 - self.num2
        mul = self.num1 * self.num2
        div = self.num1 / self.num2
        return add, sub, mul, div


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
p1 = Calc(n1, n2)
res = p1.printval()
print(res)
