class Person:
    def pdetails(self, name, age):
        self.name = name
        self.age = age


class Contact(Person):               # Multilevel inheritance
    def cdetails(self, address, email):
        self.address = address
        self.email = email


class Student(Contact):              # Multilevel inheritance
    def sdetails(self, roll_no, dept, mark):
        self.roll_no = roll_no
        self.dept = dept
        self.mark = mark
        print(self.name, self.age, self.address, self.email, self.roll_no, self.dept, self.mark)


s1 = Student()
s1.pdetails("Ram", 25)
s1.cdetails("DC", "d@g.com")
s1.sdetails(1, "CS", 200)
