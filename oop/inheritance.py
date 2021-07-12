class Person:
    def pdetails(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print(self.name, self.age, self.address)


class Student(Person):              # Single inheritance
    def sdetails(self, roll_no, dept, mark):
        self.roll_no = roll_no
        self.dept = dept
        self.mark = mark
        print(self.roll_no, self.dept, self.mark)


s1 = Student()
s1.pdetails("Ram", 25, "abc")
s1.sdetails(1, "CS", 200)
