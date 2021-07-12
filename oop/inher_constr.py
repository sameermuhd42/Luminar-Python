class Person:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def pprintval(self):
        print(self.name)
        print(self.age)


class Student(Person):
    def __int__(self, rollno, mark):
        # super().__int__(name, age)
        self.rollno = rollno
        self.mark = mark

    def sprintval(self):
        print(self.rollno)
        print(self.mark)


s1 = Student()
s1.pprintval("Ram", 22)
s1.sprintval()
