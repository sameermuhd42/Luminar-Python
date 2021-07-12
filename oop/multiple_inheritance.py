class Person:
    def pdetails(self, name, age):
        self.name = name
        self.age = age


class Contact:
    def cdetails(self, address, email):
        self.address = address
        self.email = email


class Student(Person, Contact):              # Multiple inheritance
    def sdetails(self, roll_no, dept, mark):
        self.roll_no = roll_no
        self.dept = dept
        self.mark = mark
        print(self.name, self.age, self.address, self.email, self.roll_no, self.dept, self.mark)


s1 = Student()
s1.pdetails("Ram", 25)
s1.cdetails("DC", "d@g.com")
s1.sdetails(1, "CS", 200)


# class Employee(Person, Contact):
#     def edetails(self, salary, position):
#         self.salary = salary
#         self.position = position
#         print(self.name, self.age, self.address, self.email, self.salary, self.position)
#
#
# emp1 = Employee()
# emp1.pdetails("Ram", 25)
# emp1.cdetails("DC", "d@g.com")
# emp1.edetails(20000, "Manager")
