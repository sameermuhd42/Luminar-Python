class Student:
    school_name = "XYX School"

    def setvalue(self, roll_no, name, mark):
        self.roll_no = roll_no
        self.name = name
        self.mark = mark

    def printval(self):
        print("Roll No:", self.roll_no, "\nName:", self.name, "\nMark:", self.mark, "\nSchool Name:",
              Student.school_name)


stud1 = Student()
roll = int(input("Enter roll no: "))
name1 = input("Enter the name: ")
mark1 = int(input("Enter the mark: "))
# school = input("Enter the school name: ")
stud1.setvalue(roll, name1, mark1)
stud1.printval()

stud2 = Student()
stud2.setvalue(2, "Abin", 233)
stud2.printval()
