class Person:
    def pdetails(self, name, age, address, company_name="Abc company"):
        self.name = name
        self.age = age
        self.address = address
        self.comapny_name = company_name
        print(self.name, self.age, self.address, self.comapny_name)


class Employee(Person):
    def edetails(self, salary, position):
        self.salary = salary
        self.position = position
        print(self.salary, self.position)


emp1 = Employee()
emp1.pdetails("Will", 35, "NY")
emp1.edetails(25000, "Clerk")
