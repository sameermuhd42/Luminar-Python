# Constructor: To initialize instance variables - It automatically invokes when object is created


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def printval(self):
        print(self.name, self.age, self.address)


p1 = Person("Nick", 45, "NY")
p1.printval()
