# OOP: Object Oriented Programming
# class: design pattern, blueprint
# object: real world entity
# reference: to perform operations on objects
# self: instance keyword


# class Person:
#     def setval(self, name, age):    # class method
#         self.name = name        # instance variable
#         self.age = age
#
#     def printval(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#
#
# person1 = Person()
# n = input("Enter the name: ")
# a = int(input("Enter the age: "))
# person1.setval(n, a)
# person1.printval()


class Employee:
    def setval(self, name, age, salary, comp_name):    # class method
        self.name = name        # instance variable
        self.age = age
        self.salary = salary
        self.comp_name = comp_name

    def printval(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Company Name:", self.comp_name)


emp1 = Employee()
name1 = input("Enter the name: ")
age1 = int(input("Enter the age: "))
salary1 = int(input("Enter the salary: "))
comp_name1 = input("Enter the company: ")
emp1.setval(name1, age1, salary1, comp_name1)
emp1.printval()
print(type(emp1))
