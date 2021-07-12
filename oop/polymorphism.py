# Polymorphism - many forms
# Overloading - same method name and different no. of arguments - Python does not support this


# class Operator:
#     def num(self, n1, n2):
#         self.n1 = n2
#         self.n2 = n2
#         print(self.n1 + self.n2)
#
#
# class Display(Operator):
#     def num(self, n3):
#         self.n3 = n3
#         print(self.n3)
#
#
# d1 = Display()
# d1.num(2, 5)


def product(dt, *args):
    p = 1
    for i in args:
        p = p * i
    print(p)


product('int', 4, 3, 4)
product('int', 9, 3)

# Overriding

# def add(datatype, *args):
#     # if datatype is int
#     # initialize answer as 0
#     if datatype == 'int':
#         answer = 0
#
#     # if datatype is str
#     # initialize answer as ''
#     if datatype == 'str':
#         answer = ''
#
#     # Traverse through the arguments
#     for x in args:
#         # This will do addition if the
#         # arguments are int. Or concatenation
#         # if the arguments are str
#         answer = answer + x
#
#     print(answer)
#
#
# # Integer
# add('int', 5, 6)
#
# # String
# add('str', 'Hi ', 'Geeks')

# Overriding - same method name and same no. of arguments


class Person:
    def printval(self, name):
        self.name = name
        print("Called Person method", self.name)


class Child(Person):
    def printval(self, subject):
        self.subject = subject
        print("Called Child method", self.subject)

c1 = Child()
c1.printval("abc")


