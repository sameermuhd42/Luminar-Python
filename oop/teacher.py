class Teacher:
    college_name = "XYZ College"

    def __init__(self, tid, tname, dept, sub):
        self.tid = tid
        self.tname = tname
        self.dept = dept
        self.sub = sub

    def printval(self):
        print("Teacher id:", self.tid, "\nTeacher name:", self.tname, "\nDepartment:", self.dept,
              "\nSubject:", self.sub, "\nCollege Name:", Teacher.college_name)


tr_id = int(input("Enter the teacher id: "))
name = input("Enter the name: ")
department = input("Enter the department: ")
subject = input("Enter the subject: ")
t1 = Teacher(tr_id, name, department, subject)
t1.printval()
