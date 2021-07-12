# without argument
def add():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(a + b)


def sub():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(a - b)


def mul():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(a * b)


# with argument


def add(a, b):
    print(a + b)


add(5, 8)

sub()
mul()

# with argument and return type


def add(a, b):
    return a + b


print(add(5, 4))


