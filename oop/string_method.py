# class College:
#     college_name = "xyz college"
#
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#
#     def printdet(self):
#         print(self.name, self.roll_no, College.college_name)
#
#     def __str__(self):
#         return str(self.roll_no) + self.name + College.college_name
#
#
# c1 = College("Anu", 21)
# print(c1)


class Employee:
    comp_name = "xyz company"

    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def printdet(self):
        print(self.name, self.experience, Employee.comp_name)

    def __str__(self):
        return self.name + str(self.experience) + Employee.comp_name


emp1 = Employee("Anu", 4)
print(emp1)
