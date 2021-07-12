class Student:
    def __init__(self, name, roll_no, course, marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def printval(self):
        print("Name:", self.name)
        print("Age:", self.roll_no)
        print("Course:", self.course)
        print("Marks:", self.marks)


f1 = open("stud", "r")
lines = f1.readlines()
for i in lines:
    words = i.split(",")
    name1, roll_no1, course1, marks1 = [j.strip(" ") for j in words]
    s1 = Student(name1, roll_no1, course1, marks1)
    s1.printval()
