class Person:
    def pdetails(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)


class Child(Person):
    def cdetails(self, address, email):
        self.address = address
        self.email = email
        print(self.address, self.email)


class Parent(Person):
    def prdetails(self, occupatn, salary):
        self.occupatn = occupatn
        self.salary = salary
        print(self.occupatn, self.salary)


class Student(Child, Parent):
    def sdetails(self, rollno, mark, school_name="Abc school"):
        self.rollno = rollno
        self.mark = mark
        self.school_name = school_name
        print(self.rollno, self.mark, self.school_name)


s1 = Student()
s1.pdetails('Max', 22)
s1.cdetails('NY', 'max@g.com')
s1.prdetails("Doctor", 45000)
s1.sdetails(10, 234)

