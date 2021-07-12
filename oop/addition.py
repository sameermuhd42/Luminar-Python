class Addition:
    def setval(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def printval(self):
        print("Sum: ", self.num1 + self.num2)


add1 = Addition()
n1 = int(input("Enter the n1: "))
n2 = int(input("Enter the n2: "))
add1.setval(n1, n2)
add1.printval()
