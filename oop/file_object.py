class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printval(self):
        print("Name:", self.name)
        print("Age:", self.age)


f1 = open("new", "r")
lines = f1.readlines()
for i in lines:
    words = i.split(",")
    name1, age1 = [j for j in words]
    p2 = Person(name1, age1)
    p2.printval()


# f1 = open("new", "r")
# lines = f1.readlines()
# for i in lines:
#     print(i)
#     words = i.split(",")
#     print(words)
#     name1, age1 = [j.strip(" ") for j in words]
#     print(name1)
#     print(age1)
#     p2 = Person(name1, age1)
#     p2.printval()
