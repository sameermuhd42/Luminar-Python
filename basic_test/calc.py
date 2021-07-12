def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def floor_div(a, b):
    return a // b


def expo(a, b):
    return a ** b


print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Floor Division \n6.Exponent")
while True:
    choice = int(input("Enter your choice: "))
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if choice == 1:
        print(add(num1, num2))
    elif choice == 2:
        print(sub(num1, num2))
    elif choice == 3:
        print(mul(num1, num2))
    elif choice == 4:
        print(div(num1, num2))
    elif choice == 5:
        print(floor_div(num1, num2))
    elif choice == 6:
        print(expo(num1, num2))
    break


